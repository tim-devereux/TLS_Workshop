# Workshop 1: Installing WSL, Apptainer and VSCode on Windows

## Table of Contents

1. Introduction
2. Prerequisites
3. Installing Windows Subsystem for Linux (WSL)
4. Setting Up a Linux Distribution
5. Installing Apptainer in WSL
6. Verifying Installation
7.  Installing VSCode
8. Troubleshooting
9. Conclusion

---

## 1. Introduction

This workshop will guide you through installing [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install) and [Apptainer](https://apptainer.org/) on a Windows machine. 

WSL enables you to run a Linux distribution alongside your Windows operating system without needing a virtual machine. Since a significant amount of scientific research is conducted using Linux, it is an essential skill for learning cutting-edge technologies. 

Apptainer, a container platform optimized for high-performance computing (HPC) environments, offers a convenient way to distribute software and simplify installations for Linux platforms. We use this to package RayCloudTools.


## 2. Prerequisites

- Windows 10 Version 2004 and higher (Build 19041 and higher) or Windows 11
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

## 4. Setting Up a Linux Distribution

### Step 1: Launch the Linux Distribution

1. Open the installed Linux distribution from the Start menu (e.g., Ubuntu).

### Step 2: Initial Setup

1. Set up your Linux user account by following the prompts.
2. Update the package list and upgrade installed packages by entering the following commands into the WSL terminal:

   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

## 5. Installing Apptainer in WSL

### Step 1: Install Dependencies

1. Install the necessary dependencies for Apptainer by entering the following commands into the WSL terminal one line at a time:

   ```bash
   sudo apt install -y software-properties-common
   sudo add-apt-repository -y ppa:apptainer/ppa
   sudo apt update
   sudo apt install -y apptainer
   ```


## 6. Verifying Installation

### Step 1: Verify Apptainer Installation

1. To verify that Apptainer is installed correctly, run:

   ```bash
   apptainer --version
   ```

   You should see the installed version of Apptainer.

### Step 2: Download the RayCloudToold container

1. Pull a test container image:

   ```bash
   apptainer pull docker://tdevereux/raycloudtools_latest.sif
   ```

2. Run the container:

   ```bash
   apptainer shell raycloudtools_latest.sif
   ```

3. Test the container:

   ```bash
   rayextract
   ```
You should see: 
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
4. To exit the container, we can run:

   ```bash
   exit
   ```
## 7. Install VSCode

### Step 1: Download and Install VSCode

   Visit the Visual Studio Code download page.
   Download the installer for Windows and run it.

### Step 2: Install WSL Extension for VSCode

   Open VSCode after installation.
   Click on the Extensions view icon on the Sidebar or press Ctrl+Shift+X.
   Search for the Remote - WSL extension and install it.

### Step 3: Connect VSCode to WSL

   Open a WSL terminal (e.g., Ubuntu) from the Start menu.
   In the WSL terminal, navigate to your project directory or any directory you want to work in.
   Type code . to open the current directory in VSCode. This will connect VSCode to your WSL environment.

## 8. Troubleshooting

### Common Issues and Solutions

1. **WSL Installation Issues**: Ensure that you are running the latest version of Windows 10 or 11 and that all Windows updates are installed.

2. **Linux Distribution Issues**: If the distribution does not launch correctly, try reinstalling it from the Microsoft Store.

3. **Dependency Issues**: If dependencies fail to install, check for error messages and ensure that your package list is up to date.

## 9. Conclusion

You have successfully installed WSL and Apptainer on your Windows machine. This setup allows you to leverage the power of Linux within a Windows environment

---

For additional help or information, refer to the official [WSL documentation](https://docs.microsoft.com/en-us/windows/wsl/) and [Apptainer documentation](https://apptainer.org/docs/).