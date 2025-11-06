import os

os.remove("chapter5/index.html")

os.rmdir("chapter5/new_folder")  # Remove empty folder

# How to delete a folder that is not empty?
# 1. os.walk() to traverse and delete files first, then delete folders
# 2. Use shutil.rmtree() to delete a folder and all its contents
