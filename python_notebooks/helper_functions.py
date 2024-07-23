import pandas as pd

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


import numpy as np

def icp(source, target, max_iterations=100, tolerance=1e-6):
    """
    Perform Iterative Closest Point (ICP) to align target to source.

    Parameters:
    source (np.ndarray): Source point set (Nx2).
    target (np.ndarray): Target point set (Nx2).
    max_iterations (int): Maximum number of iterations to run ICP.
    tolerance (float): Convergence tolerance.

    Returns:
    np.ndarray: Aligned target point set.
    np.ndarray: Final transformation matrix.
    """
    def best_fit_transform(A, B):
        """
        Calculate the best-fit transform that maps points A to points B.

        Parameters:
        A (np.ndarray): Source point set (Nx2).
        B (np.ndarray): Target point set (Nx2).

        Returns:
        np.ndarray: Rotation matrix (2x2).
        np.ndarray: Translation vector (2x1).
        """
        centroid_A = np.mean(A, axis=0)
        centroid_B = np.mean(B, axis=0)
        
        AA = A - centroid_A
        BB = B - centroid_B
        
        H = np.dot(AA.T, BB)
        U, S, Vt = np.linalg.svd(H)
        
        R = np.dot(Vt.T, U.T)
        
        if np.linalg.det(R) < 0:
            Vt[1, :] *= -1
            R = np.dot(Vt.T, U.T)
        
        t = centroid_B.T - np.dot(R, centroid_A.T)
        
        return R, t

    prev_error = float('inf')
    target_copy = target.copy()
    
    for i in range(max_iterations):
        distances = np.linalg.norm(source[:, np.newaxis] - target_copy[np.newaxis, :], axis=2)
        closest_point_indices = np.argmin(distances, axis=1)
        
        closest_points = target_copy[closest_point_indices]
        
        R, t = best_fit_transform(source, closest_points)
        
        target_copy = np.dot(target_copy, R.T) + t.T
        
        mean_error = np.mean(np.linalg.norm(source - closest_points, axis=1))
        
        if np.abs(prev_error - mean_error) < tolerance:
            break
        
        prev_error = mean_error
    
    return target_copy, np.vstack((np.hstack((R, t[:, np.newaxis])), np.array([0, 0, 1])))