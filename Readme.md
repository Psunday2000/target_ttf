# TTF Files Copying Tool

### A Python Program that targets ttf files and copies them to another location

This is a Python script that automates the process of copying TrueType Font (TTF) files from subdirectories to the Windows/fonts folder. This can be useful for managing fonts on your Windows system.

## Problem Description

If you have a directory containing subdirectories, each containing TTF files, the goal is to copy these TTF files to the Windows/fonts folder.

## Algorithm

1. **List Directories and Files:**

   - Navigate to the root directory containing subdirectories.
   - Recursively traverse through the directories to find TTF files.

2. **Identify TTF Files:**

   - For each directory, list the files it contains.
   - Check if each file has a ".ttf" extension to identify TTF files.

3. **Copy TTF Files:**
   - Once a TTF file is identified, copy it to the Windows/fonts directory.
   - Ensure that you have the necessary permissions to write to the Windows/fonts folder.

## How to Run

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/psunday2000/target_ttf.git
   ```
