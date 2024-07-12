# Extracting dense voxels from RIEGL terrestrial scanner data

## Overview

This guide explains how to extract plot level forest structural information using RayCloudTools.
## Prerequisites

- **Dependencies**: Ensure you have WSL with the RayCloudTools container.
- **Data Preparation**: You should have an already coregistered plot level point cloud as LAZ v1.2.

## Workflow Steps

### 1. Importing Data

#### Unbound Data


To import point cloud data to use is RCT, we use the command rayimport:

Example command:

```bash
rayimport cloud.las 0,0,0
```

### 2. Clipping Data to Plot Boundary

Next, clip the point cloud to the plot boundary using 'raysplit capsule'. This command splits within a cylindrical capsule using the cylinder start, end and radius. If the plot centre coordinate is not already known, we can determine this using CloudCompare. We already know the plot centre is 0,0,0, and the plot radius is 25m. The the Z upper bound is set to 30m (should be more than the tallest tree), and the Z lower bound is set as -10 to capture any data below 0. This will give use the following command: 

```bash
raysplit cloud_raycloud.ply capsule 0,0,-10 0,0,30 25
```

### 3. Extracting terrain

Extract the digital terrain model, this is required to determine the base of trees in the subsequent step. 

```bash
rayextract terrain cloud_raycloud_inside.ply
```


### 4. Extracting trees

Extract the trees using the final raycloud (undecimated) and the terrain mesh:

```bash
rayextract trees cloud_raycloud_inside.ply cloud_raycloud_inside_mesh.ply
```

### 5. Computing tree metrics

```bash
treeinfo trees cloud_raycloud_inside_tree.txt
```