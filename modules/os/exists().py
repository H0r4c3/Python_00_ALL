import os

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\os'

# Check whether the specified path exists or not
pathExists = os.path.exists(path)
print(f'Path exists = {pathExists}')