# UR5 Forward Kinematics Using Python

## 1. Project Overview

This project implements the Forward Kinematics of a modified UR5 six-degree-of-freedom (6-DOF) robotic manipulator using Python.

The Standard Denavit-Hartenberg (DH) convention is used to calculate the transformation matrices and determine the end-effector position and orientation.

## 2. Robot Specifications

- Robot: Modified UR5
- Degrees of Freedom: 6
- DH Convention: Standard DH
- Programming Language: Python
- Library: NumPy
- Robot Dimensions: Increased by 5%
- Joint Angles: [30°, 45°, 30°, 20°, 60°, 90°]

## 3. Project Objectives

- Understand the Denavit-Hartenberg convention.
- Calculate individual joint transformation matrices.
- Perform forward kinematics using homogeneous transformation matrices.
- Determine the final end-effector position and orientation.

## 4. Methodology

The forward kinematics equation is:

T = A1 × A2 × A3 × A4 × A5 × A6

Each transformation matrix is calculated using the Standard DH parameters.

Python and NumPy are used for matrix calculations.

## 5. Installation

Install Python and NumPy.

```bash
pip install numpy
```

## 6. How to Run

Run the following command:

```bash
python ur5_forward_kinematics.py
```

## 7. Output

The program displays:

- Six individual transformation matrices.
- Final homogeneous transformation matrix.
- End-effector position in millimetres.

## 8. Technologies Used

- Python
- NumPy
- GitHub

## 9. Applications

- Industrial robotics
- Robotic manipulator design
- Robot kinematics
- Coordinate transformations
- Robotics research and development

## 10. Author

Mechanical Engineering | Robotics Engineering

**Project:** UR5 Forward Kinematics
