# Method 1: importing the entire module
import math

print(math.sqrt(16))

# Method 2: importing the entire module with an alias
import random as rd

print(rd.randint(1, 10))

# Method 3: importing the entire module using wildcard(*)
from datetime import *

print(date.today())

# Method 4: importing specific functions or classes from a module
from os import path

print(path.exists("somefile.txt"))
