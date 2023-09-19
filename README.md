# python

# Table of Contents

1. [Exercise 1](#exercise-1)

# Exercise 1

## Table of Contents

1. [Install Python](#install-python)
2. [Set Up a Virtual Environment](#set-up-a-virtual-environment)
3. [Create a Python Script](#create-a-python-script)
4. [Set Up IPython Shell](#set-up-ipython-shell)
5. [Export a Requirements File](#export-a-requirements-file)


## Install Python

Install Python 3.8.7 on your system. Check your Python version by using the command `python --version` from your terminal.

![Step 1](./exercise-1.1/screenshots/step_1.jpg)

## Set Up a Virtual Environment

Set up a new virtual environment named “cf-python-base”.

![Step 2](./exercise-1.1/screenshots/step_2.jpg)

## Create a Python Script

Using your IDE create a Python script file "add.py". This script will prompt user to input 2 numbers to be added and print the the result.

![Step 3](./exercise-1.1/screenshots/step_3.jpg)

```
#Prompt user to enter numbers for two variables
a = int(input("Enter a first number to be added."))
b = int(input("Enter a second number to be added."))

#The two numbers are added and value is stored in C
c = a + b

#display the value of the two added numbers
print(c)
```

## Set Up IPython Shell

Use pip to install IPython shell in the virtual environment "cf-python-base".

![Step 4](./exercise-1.1/screenshots/step_4.jpg)

## Export a Requirements File

use "pip freeze > requirements.txt" to enerate a "requirements.txt" file for "cf-python-base". Use "mkvirtualenv" to create a new environment called "cf-python-copy". Use "pip install -r requirements.txt" to install the packages from the "requirements.txt" file.

![Step 5](./exercise-1.1/screenshots/step_5.jpg)