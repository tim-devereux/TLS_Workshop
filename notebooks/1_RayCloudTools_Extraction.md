### Notebook 1 - Extracting Tree Structural Metrics using RayCloudTools

#### Overview

This guide explains how to extract plot level forest structural information using RayCloudTools (RCT). This notebook contains commands to be copied and run within the RTC shell. If you need usage information for any of the tools, you can type the tool name in the shell to return usage information (e.g. ```rayextract```).

#### Prerequisites

- **Dependencies**: Ensure you installed VSCode and WSL with the RayCloudTools container.
- **Environment**: You should have this repository open in VSCode, using WSL as the host.
- **Data Preparation**: You should have an already coregistered plot level point cloud as PLY or LAZ v1.2.

### Workflow Steps

#### 1. Enter the RCT container shell

Enter the RTC container shell by running the following command in the WSL terminal - 

```
apptainer shell raycloudtools_latest.sif
```

#### 2. Navigate to the data directory
You can change the current directory within the terminal using the ```cd``` command -

``
cd TLS_Workshop/data
``

List the contents of the current directory - 

```
ls
```

You should see the point cloud data and the inventory data listed. 

#### 3. Importing Data

To import point cloud data to use in RCT, we use the ```rayimport``` tool. Some funtionality within RCT uses the trajectories of LiDAR pulses to calcuate density. This information is not needed to get woody volume, so we can set the ray trajectories to 0,0,-10 for all pulses using ```ray 0,0,-10```. RCT also uses pulse return intensity to detmine whether a pulse hits or misses, this is not needed either so we set them all to hits (descreet points) using ```--max_intensity 0```.

To import data from a point cloud without unique pulse trajectories and with all data as hits, use the following command:

```
rayimport Mak1_clipped.ply ray 0,0,-10 --max_intensity 0
```

#### 4. Clipping Data to Plot Boundary

Next, we clip the point cloud to the plot boundary using ```raysplit capsule```. This command splits within a cylindrical capsule using the cylinder start, end and radius. If the plot centre coordinate is not already known, we can determine this using the CloudCompare point picking tool. We already know the plot centre for our data is 2,12,0, and the plot radius is 25m. The Z upper bound is set to 30m (should be more than the tallest tree), and the Z lower bound is set as -10 to capture any data below 0. This will give us the following command which should be run in the terminal: 
```
raysplit Mak1_clipped_raycloud.ply capsule 2,12,-10 2,12,30 20
```
The output is 2 separate files, '_inside.ply' and '_outside.ply'. The data within our plot will have the '_inside.ply' suffix. This is the data we will use in the subsequent steps. You can load this data into CloudCompare to check that you've clipped it correctly.

#### 5. Extracting terrain

Here we extract the digital terrain model, this is required to determine the base of trees in the subsequent step. 
```
rayextract terrain Mak1_clipped_raycloud_inside.ply
```
The ouput is a 3D mesh, which deliniates the contours of the ground. Load this into CloudCompare to check the quality. 

#### 6. Extracting trees using 'rayextract trees'

Extract trees using the raycloud and the terrain mesh as input:
```
rayextract trees Mak1_clipped_raycloud_inside.ply Mak1_clipped_raycloud_inside_mesh.ply
```
rayextract trees will generate three outputs:

1. A segmented raycloud, where each tree is uniquely colored.
2. A 3D mesh representing the woody components (stems and branches).
3. A trees.txt file containing cylinder data representing the tree structural models. All tree metrics are derived from these models.

The segmented raycloud and the woody mesh can also be visualised in CloudCompare. It is important to check the quality of the individual tree segmentaion and the tree cylinder models as this will affect the accuracy of our metrics.

#### 7. Computing tree metrics

Finally, we compute a set of common metrics from the structural models using the ```treeinfo``` command. This tools is part of a separate library 'treetools', but is also available within the container.  

```
treeinfo Mak1_clipped_raycloud_inside_trees.txt
```

This will produce another .txt file with the suffix '_trees_info.txt'. This file contains the additional metrics per tree.  This file and 'trees.txt' contain all the data that is used in the subsequent Python anlysis. 
