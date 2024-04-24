# Objectives

# The Python library “os” must be utilized
# At least three variables must be declared in Python that contain bash operations
# Use the python os function to print the following commands below.  These are bash commands and we are going to run them through a python script.
# Add description printed to the terminal of what is about to run



# whoami
# ip a
# lshw -short
# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.
# Instead of os.system() function, utilize the subprocess module instead. Refer to python.org for how this can be achieved.



# This will not run on windows needs to be mac or linux due to os being bash

import subprocess
import os

results1 = subprocess.run(['whoami'], capture_output=True, text=True)
print('Now running whoami command')
print('results:', results1.stdout)

results2 = subprocess.run(['ip', 'a'], capture_output=True, text=True)
print('Now running ip a command')
print('results:', results2.stdout)

results3 = subprocess.run(['lshw', '-short'], capture_output=True, text=True)
print('Now running lshw -short command')
print('results:', results3.stdout)