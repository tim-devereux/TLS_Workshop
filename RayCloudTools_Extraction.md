# Extracting Tree Structural Metrics using RayCloudTools

## Overview

This guide explains how to extract plot level forest structural information using RayCloudTools (RCT).

## Prerequisites

- **Dependencies**: Ensure you installed VSCode and WSL with the RayCloudTools container.
- **Environment**: You should have this repository open in VSCode, using WSL as the host.
- **Data Preparation**: You should have an already coregistered plot level point cloud as LAZ v1.2.

## Workflow Steps

### 1. Enter the container by running the following command in the WSL terminal - 

```
apptainer shell raycloudtools_latest.sif
```
### 1. Importing Data

To import point cloud data to use in RCT, we use the ```rayimport``` tool. Some funtionality within RCT uses the trajectores of LiDAR pulses to calcuate density. This information is not needed to get woody volume, so we can set the scanner position to 0,0,-10 for all pulses. 


To import data from a point cloud without lidar pulse trajectories, use the following command:

```
rayimport Mak1_clipped.ply ray 0,0,-10 --max_intensity 0
```

### 2. Clipping Data to Plot Boundary

Next, clip the point cloud to the plot boundary using 'raysplit capsule'. This command splits within a cylindrical capsule using the cylinder start, end and radius. If the plot centre coordinate is not already known, we can determine this using the CloudCompare point picking tool. We already know the plot centre is 0,0,0, and the plot radius is 25m. The Z upper bound is set to 30m (should be more than the tallest tree), and the Z lower bound is set as -10 to capture any data below 0. This will give use the following command: 
```
raysplit Mak1_clipped_raycloud.ply capsule 2,12,-10 2,12,30 20
```
The output is 2 separate files, '_inside.ply' and '_outside.ply'. The data within our plot will have the '_inside.ply' suffix. This is the data we will use in the subsequent steps. 

### 3. Extracting terrain

Here we extract the digital terrain model, this is required to determine the base of trees in the subsequent step. 
```
rayextract terrain Mak1_clipped_raycloud_inside.ply
```
The ouput with be a 3D mesh, which deliniates the contours of the ground.

### 4. Extracting trees using 'rayextract trees'

Extract trees using the raycloud and the terrain mesh as input:
```
rayextract trees Mak1_clipped_raycloud_inside.ply Mak1_clipped_raycloud_inside_mesh.ply
```
rayextract trees will generate three outputs:

1. A segmented raycloud, where each tree is uniquely colored.
2. A 3D mesh representing the woody components (stems and branches).
3.  A trees.txt file containing cylinder data representing the tree structural models. All tree metrics are derived from these models.

### 5. Computing tree metrics

Finally, we compute a set of common metrics from the structural models using ```treeinfo```. 

```
treeinfo Mak1_clipped_raycloud_inside_trees.txt
```

This will produce another .txt file with the suffix '_trees_info.txt'. This file contains the additional metrics per tree.  This file and 'trees.txt' contain all the data that is used in the subsequent python anlysis. 