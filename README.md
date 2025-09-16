# Overview

Welcome to the TLS workshop Git repository! This repository contains detailed instructions on extracting tree metrics from terrestrial laser scanner (TLS) point clouds using RayCloudTools (RCT) and Python notebooks. 

Before cloning this repository and running the Python notebooks, it will be necessary to install VSCode, WSL and Docker. To start, follow the instructions below.

![Processed TLS](processed_tls.png)

---

## Required Software

This markdown will guide you through installing [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install), [Docker](https://www.docker.com/), and [VSCode](https://code.visualstudio.com/) on a Windows machine.

WSL enables you to run a Linux distribution alongside your Windows operating system without needing a virtual machine. Since a significant amount of scientific research is conducted using Linux, it is an essential skill for learning new technologies.

Docker, a containerization platform, offers a convenient way to distribute software and simplify installations across different platforms. We use this to package RayCloudTools.

[Visual Studio Code (VSCode)](https://code.visualstudio.com/) is an open-source code editor developed by Microsoft. It supports a wide range of programming languages and frameworks, making it an ideal tool for data analysis. With the [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) extension, you can seamlessly connect and work within your WSL environment.


## Prerequisites

- Windows 11 or Windows 10 Version 2004 and higher (Build 19041 and higher)
- Administrative privileges on the Windows machine
- An internet connection


## Download and Install CloudCompare

   If not already installed on your machine, download the CloudCompare installer for your operating system from [here](https://www.danielgm.net/cc/) and install using defaults. 

## Installing Windows Subsystem for Linux (WSL)

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

4. Install Python and other dependencies in WSL

   ```
   sudo apt install python3 python3-pip ipython3
   ```

## Installing Docker in WSL

### Step 1: Install Dependencies

Install the necessary dependencies for Docker by entering the following command into the WSL terminal:

   ```bash
   sudo apt install -y ca-certificates curl gnupg lsb-release
   ```
### Step 2: Add Docker's Official GPG Key
Add Docker's official GPG key:
   ```bash
   sudo mkdir -p /etc/apt/keyrings
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   ```
### Step 3: Set Up the Repository
Set up the Docker repository:
   ```bash
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```
### Step 4: Install Docker Engine
Update the package index and install Docker:
   ```bash
   sudo apt update && sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   ```
### Step 5: Start Docker Service
Start and enable the Docker service:
   ```bash
   sudo systemctl start docker
   sudo systemctl enable docker
   ```
### Step 6: Add User to Docker Group
Add your user to the docker group to run Docker commands without sudo:
   ```bash
   sudo usermod -aG docker $USER
   ```
Log out and log back in for the group changes to take effect.

To verify that Docker is installed correctly, run:

   ```bash
   docker --version
   ```
You should see the installed version of Docker (e.g. Docker version 24.0.7, build afdd53b).

## Install the RayCloudtools Docker Image

### Step 1: Pull the RayCloudTools container image:

To download the RayCloudTools container:

   ```bash
   docker pull ghcr.io/csiro-robotics/raycloudtools:latest
   ```
### Step 2: Run the RayCloudTools container:

To run and enter the container interactively:

   ```bash
   docker run -it --rm ghcr.io/csiro-robotics/raycloudtools:latest bash
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
## Installing VSCode

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


## Cloning the Workshop Repository in VSCode
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

## Conclusion

That is everything for need to comtinue! You have successfully installed WSL, Docker, and VSCode on your Windows machine. You have cloned a Git repository and configured a software container to run RayCloudTools. In the next workshop we will learn to use what we have installed here to extract tree metrics from point cloud data using RCT and analyse the output using Python.

For additional help or information, refer to the official [WSL documentation](https://docs.microsoft.com/en-us/windows/wsl/), [Visual Studio Code documentation](https://code.visualstudio.com/docs), and [Docker documentation](https://docs.docker.com/).

---
