import sys

# import not_existing_module  # ModuleNotFoundError will be raised here

print(sys.path)

# Modify sys.path to Include the Directory of Your Modules

# 1. use sys.path.append()
sys.path.append("/path/to/your/module_directory")

# 2. modify the pythonpath environment variable

# 3. create a sitecustomize.py file
# and place it in the site-packages directory
# with the following content:
# import site
# site.addsitedir('/path/to/your/module_directory')
