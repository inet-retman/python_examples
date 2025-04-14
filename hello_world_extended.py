import sys
import time
import datetime

print('Hello World! This program is written in Python.')
print('Generating Some Data....be patient!..........\n')

#To add excitement
for x in range(2):
    time.sleep(1)
    print("....")

# Let's Use an F String to print out the version of python executing this script

python_system_version = sys.version_info
print("")
print(f"Python Version {python_system_version[0]}.{python_system_version[1]}.{python_system_version[2]}")

# Let's see what time and day it is

x  = datetime.datetime.now().astimezone() # Make datetime aware of the local time

print(f"Today is {x.strftime('%A,%B %d,%Y')}")
print(f"Current Time is {x.strftime('%H:%M:%S.%f')} in the {x.strftime('%Z')} zone")

#To add excitement
for x in range(2):
    time.sleep(1)
    print("....")

print("Goodbye!")
