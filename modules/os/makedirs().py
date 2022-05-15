'https://appdividend.com/2021/07/03/how-to-create-directory-if-not-exist-in-python/'

import os

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\os1\New Folder'

# Check whether the specified path exists or not
pathExists = os.path.exists(path)


if pathExists == False:
    os.makedirs(path)
    print('New Folder created!')
else:
    print(f'Path exists = {pathExists}!')