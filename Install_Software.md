# Workshop 1: Installing Software

##  Contents

1. Introduction
2. Prerequisites
3. Installing Windows Subsystem for Linux (WSL)
4. Installing Apptainer in WSL
5. Installing RayCloudTools Container
6. Installing VSCode
7. Cloning respository in VSCode
8. Conclusion

---

## 1. Introduction

This notebook will guide you through installing [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install), [Apptainer](https://apptainer.org/), and [VSCode](https://code.visualstudio.com/) on a Windows machine.

WSL enables you to run a Linux distribution alongside your Windows operating system without needing a virtual machine. Since a significant amount of scientific research is conducted using Linux, it is an essential skill for learning new technologies.

Apptainer, a container platform optimized for high-performance computing (HPC) environments, offers a convenient way to distribute software and simplify installations for Linux platforms. We use this to package RayCloudTools.

[Visual Studio Code (VSCode)](https://code.visualstudio.com/) is an open-source code editor developed by Microsoft. It supports a wide range of programming languages and frameworks, making it an ideal tool for data analysis. With the [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) extension, you can seamlessly connect and work within your WSL environment.


## 2. Prerequisites

- Windows 11 or Windows 10 Version 2004 and higher (Build 19041 and higher)
- Administrative privileges on the Windows machine
- An internet connection

## 3. Installing Windows Subsystem for Linux (WSL)

### Step 1: Enable WSL

1. Open PowerShell as an Administrator. To do this, right-click on the Start button and select "Windows PowerShell (Admin)" or "Command Prompt (Admin)".
   
2. Enter the following command to enable WSL:

   ```powershell
   wsl --install
   ```

   This command will enable the required features and install the default Linux distribution (Ubuntu).

2. Follow the on-screen instructions to complete the installation.

### Step 2: Setting Up a Linux Distribution

1. Open the installed Linux distribution from the Start menu (Ubuntu).
2. Set up your Linux user account by following the prompts. You will need to provide a username and password.
3. Update the package list and upgrade installed packages by entering the following commands into the WSL terminal:

   ```
   sudo apt update
   ```
   ```
   sudo apt upgrade -y
   ```

## 4. Installing Apptainer in WSL

### Step 1: Install Dependencies

Install the necessary dependencies for Apptainer by entering the following command into the WSL terminal:

   ```bash
   sudo apt install -y software-properties-common
   ```
### Step 2: Install Apptainer
To install Apptainer we need to add the remote repository, this is the location online that WSL will look to download the software.
   ```
   sudo add-apt-repository -y ppa:apptainer/ppa
   ```
And now that the repository is added, we can download and install Apptainer.
   ```bash
   sudo apt -y update && sudo apt install -y apptainer
   ```
To verify that Apptainer is installed correctly, run:

   ```bash
   apptainer --version
   ```
You should see the installed version of Apptainer (e.g. apptainer version 1.3.2-1).

## 5. Install the RayCloudtools Container

### Step 1: Pull the RayCloudTools container image:

To download the RayCloudTools container:

   ```bash
   apptainer pull docker://tdevereux/raycloudtools_latest.sif
   ```
### Step 2: Run the RayCloudTools container:

To run and enter the container:

   ```bash
   apptainer shell raycloudtools_latest.sif
   ```

Test the container by running a RayCloudTools command:

   ```bash
   rayimport
   ```
If all is well, you should see - 
   ```
   Import a point cloud and trajectory file into a ray cloud
   usage:
   rayimport pointcloudfile trajectoryfile  - pointcloudfile can be a .laz, .las or .ply file
                                             trajectoryfile is a text file using 'time x y z' format per line
   rayimport pointcloudfile 0,0,0           - use 0,0,0 as the sensor location
   rayimport pointcloudfile ray 0,0,-10     - use 0,0,-10 as the constant ray vector from start to point
                                          --max_intensity 100 - specify maximum intensity value (default 100).
                                                               0 sets all to full intensity (bounded rays).
                                          --remove_start_pos  - translate so first point is at 0,0,0
   The output is a .ply file of the same name (or with suffix _raycloud if the input was a .ply file).
   ```
To exit the container and return to WSL:

   ```bash
   exit
   ```
## 6. Installing VSCode

### Step 1: Download and Install VSCode

   Visit the [Visual Studio Code download page](https://code.visualstudio.com/download).
   Download the installer for Windows and install using defaults.

### Step 2: Install WSL Extension for VSCode

   Open VSCode after installation.
   Click on the Extensions view icon on the Sidebar or press Ctrl+Shift+X.
   Search for the Remote - WSL extension and install it by clicking on the green install icon.

### Step 3: Connect VSCode to WSL

   Open a WSL terminal (Ubuntu) from the Start menu as before.
   In the WSL terminal, input ```code .``` to open the current directory in VSCode. This will connect VSCode to your WSL environment.




## 7. Cloning a Repository in VSCode
### Step 1: Clone the Repository

   In VSCode, press Ctrl+Shift+P to open the Command Palette.



   Type ```Git: Clone``` and select it from the dropdown options.

   Enter the repository URL:
   ```
   https://github.com/tim-devereux/TLS_Workshop.git
   ```
   Choose a directory where you want to clone the repository, your user directory within WSL is appropriate (/home/username).

### Step 2: Open the Cloned Repository

   Once the cloning process is complete, you will be prompted to open the cloned repository. Click "Open" to open the project in VSCode.


## 8. Conclusion

That is everything for this component! You have successfully installed WSL, Apptainer, and VSCode on your Windows machine. You have cloned a Git repository and configured a software container to run RayCloudTools. In the next workshop we will learn to use what we have installed here to extract tree metrics from point cloud data using RCT and analyse the output using Python.

For additional help or information, refer to the official [WSL documentation](https://docs.microsoft.com/en-us/windows/wsl/), [Visual Studio Code documentation](https://code.visualstudio.com/docs), and [Apptainer documentation](https://apptainer.org/docs/).

---
