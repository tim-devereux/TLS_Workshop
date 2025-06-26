import pandas as pd
import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation as R
from scipy.spatial import cKDTree

def treeinfo_attributes_tree(tree_file):
    """
    Extracts per-tree tree attributes from a tree file generated using treeinfo and returns a DataFrame. 
    Can be run on a 'forest' or single treefile.

    Parameters:
    tree_file (str): The path to the treefile.

    Returns:
    pandas.DataFrame: A DataFrame containing tree attributes. If the input file is a forest, the DataFrame will contain a column 'tree_id' with the tree ID.
    """
    line_list = []
    with open(tree_file, 'r') as file:
        lines = file.readlines()
        line_count = 0        
        for line in lines:
            data = line.split(', ')
            for row in data:
                section_data = row.strip().split(', ')
                cell_data = section_data[0].strip().split(',')
                if len(cell_data) == 7:
                    line_list.append(cell_data)
            line_count += 1
    df = pd.DataFrame(line_list[1:], columns=line_list[0]).astype(float)
    if len(df) > 1:
        df.insert(0, 'tree_id', range(1, len(df) + 1)) 
        
    return df

def treeinfo_attributes_segment(tree_file):
    """
    Extracts per-segment attributes of a tree file generated using treeinfo and returns a DataFrame.
    Can be run on a 'forest' or single treefile.

    Parameters:
    tree_file (str): The path to the treefile created using treeinfo.

    Returns:
    pandas.DataFrame: A DataFrame containing segment attributes. If the input file is a forest, the DataFrame will contain a column 'tree_id' with the tree ID.
    """
    line_list = []
    tree_ids = []
    tree_id = 0
    
    with open(tree_file, 'r') as file:
        lines = file.readlines()
        line_count = 0        
        for line in lines:
            data = line.split(', ')
            for row in data:
                section_data = row.strip().split(', ')
                cell_data = section_data[0].strip().split(',')
                if len(cell_data) == 7 and all(x.replace('.', '', 1).isdigit() for x in cell_data):
                    tree_id += 1
                if len(cell_data) > 7:
                    if tree_id != 0:
                        tree_ids.append(tree_id)
                    line_list.append(cell_data)
            line_count += 1
    df = pd.DataFrame(line_list[1:], columns=line_list[0]).astype(float)
    df.insert(0, 'tree_id', tree_ids)
    # remove row where parent_id is -1.0
    df = df[df['parent_id'] != -1.0]
    return df

def attributes_tree(tree_file):
    """
    Extracts per-tree tree attributes from a tree file generated using rayextract trees and returns a DataFrame. 
    Can be run on a 'forest' or single treefile.

    Parameters:
    tree_file (str): The path to the treefile created using rayextract.

    Returns:
    pandas.DataFrame: A DataFrame containing tree attributes. If the input file is a forest, the DataFrame will contain a column 'tree_id' with the tree ID.
    """
    tree_ids = []
    line_list = []
    tree_id = 0

    with open(tree_file, 'r') as file:
        lines = file.readlines()
        line_count = 0        
        for line in lines[1:]:
            data = line.split(', ')
            for row in data:
                cell_data = data[0].strip().split(',')
                line_list.append(cell_data)
                tree_id += 1
            line_count += 1
    df = pd.DataFrame(line_list[2:], columns=line_list[0]).astype(float)
    # remove duplicate rows
    df = df.drop_duplicates()

    if len(df) > 1:
        df.insert(0, 'tree_id', range(1, len(df) + 1)) 

    return df

def nearest_neighbor(src, dst):
    """ Find the nearest (Euclidean) neighbor in dst for each point in src. """
    tree = cKDTree(dst)
    distances, indices = tree.query(src)
    return distances, indices

def icp(source, target, init_pose=None, max_iterations=50, tolerance=1e-5):
    """ The Iterative Closest Point method """
    src = np.copy(source)
    dst = np.copy(target)

    if init_pose is not None:
        src = np.dot(src, init_pose[:3, :3].T) + init_pose[:3, 3]

    prev_error = 0

    for i in range(max_iterations):
        distances, indices = nearest_neighbor(src, dst)

        T = best_fit_transform(src, dst[indices])
        src = np.dot(src, T[:3, :3].T) + T[:3, 3]

        mean_error = np.mean(distances)
        if np.abs(prev_error - mean_error) < tolerance:
            break
        prev_error = mean_error

    T = best_fit_transform(source, src)
    return T, distances

def best_fit_transform(A, B):
    """ Calculates the least-squares best-fit transform that maps A to B """
    assert len(A) == len(B)

    # Find the centroids
    centroid_A = np.mean(A, axis=0)
    centroid_B = np.mean(B, axis=0)

    # Center the points
    AA = A - centroid_A
    BB = B - centroid_B

    # Dot is matrix multiplication for array
    H = np.dot(AA.T, BB)

    # Find the rotation using SVD
    U, S, Vt = np.linalg.svd(H)
    R = np.dot(Vt.T, U.T)

    # Special reflection case
    if np.linalg.det(R) < 0:
        Vt[-1, :] *= -1
        R = np.dot(Vt.T, U.T)

    t = centroid_B.T - np.dot(R, centroid_A.T)

    # Create the transformation matrix
    T = np.identity(4)
    T[:3, :3] = R
    T[:3, 3] = t

    return T
