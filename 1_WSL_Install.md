## Workshop 1: Installing WSL and Apptainer on Windows

## Table of Contents

1. Introduction
2. Prerequisites
3. Installing Windows Subsystem for Linux (WSL)
4. Setting Up a Linux Distribution
5. Installing Apptainer in WSL
6. Verifying Installation
7. Troubleshooting
8. Conclusion

---

## 1. Introduction

This workshop will guide you through the process of installing Windows Subsystem for Linux (WSL) and Apptainer on a Windows machine. WSL allows you to run a Linux distribution alongside your Windows operating system without the need for a virtual machine. Apptainer is a container platform optimized for high-performance computing (HPC) environments.

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

   This command will enable the required features and install the default Linux distribution.

2. Follow the on-screen instructions to complete the installation.

## 4. Setting Up a Linux Distribution

### Step 1: Launch the Linux Distribution

1. Open the installed Linux distribution from the Start menu (e.g., Ubuntu).

### Step 2: Initial Setup

1. Set up your Linux user account by following the prompts.
2. Update the package list and upgrade installed packages:

   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

## 5. Installing Apptainer in WSL

### Step 1: Install Dependencies

1. Install the necessary dependencies for Apptainer:

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
   apptainer shell --bind /mnt:/mnt raycloudtools_latest.sif
   ```

3. Exit the container:

   ```bash
   exit
   ```


## 7. Troubleshooting

### Common Issues and Solutions

1. **WSL Installation Issues**: Ensure that you are running the latest version of Windows 10 or 11 and that all Windows updates are installed.

2. **Linux Distribution Issues**: If the distribution does not launch correctly, try reinstalling it from the Microsoft Store.

3. **Dependency Issues**: If dependencies fail to install, check for error messages and ensure that your package list is up to date.

## 8. Conclusion

You have successfully installed WSL and Apptainer on your Windows machine. This setup allows you to leverage the power of Linux containers within a Windows environment, enabling a versatile and powerful development workflow.

---

For additional help or information, refer to the official [WSL documentation](https://docs.microsoft.com/en-us/windows/wsl/) and [Apptainer documentation](https://apptainer.org/docs/).