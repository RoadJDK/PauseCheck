# PauseCheck

## Overview
PauseCheck is a tool designed for teachers to track their students' breaks. It helps in monitoring break durations and ensures students return on time. This tool is especially useful in managing break times during classes or study sessions.

## Setup

### Step 1: Install Dependencies
- You need to have Python installed on your system.
- Install the required Python package `plyer`:
`pip install plyer`

### Step 2: Prepare the Student List
- Create a text file named `student_list.txt`.
- Enter the names of your students in this file, each name on a new line.

### Step 3: Start the Program
- Run `main.py` from your Python environment.
- Ensure that `student_list.txt` is in the same directory as `main.py`.

## Usage

### Starting a Break
- To track a new break for a student, type:

start break [Name]

Replace `[Name]` with the student's name.


### Ending a Break
- When a student returns from their break, type:

end break [Name]

Again, replace `[Name]` with the student's name.


### Monitoring Breaks
- The program will display the current active breaks.
- If a student exceeds their break time, you will receive a Windows notification.

## Features
- Easy tracking of student break times.
- Notifications for break time exceedances.
- Simple and user-friendly interface.

## Note
This tool is designed to assist teachers in managing classroom break times effectively. It should be used to promote a structured and disciplined learning environment.
