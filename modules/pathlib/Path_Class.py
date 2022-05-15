'https://docs.python.org/3/library/pathlib.html'

'''
If you’ve never used this module before or just aren’t sure which class is right for your task, Path is most likely what you need. 
It instantiates a concrete path for the platform the code is running on.

Pure paths are useful in some special cases; for example:

If you want to manipulate Windows paths on a Unix machine (or vice versa). You cannot instantiate a WindowsPath when running on Unix, but you 
can instantiate PureWindowsPath.

You want to make sure that your code only manipulates paths without actually accessing the OS. In this case, instantiating one of the pure classes may be 
useful since those simply don’t have any OS-accessing operations.
'''

from pathlib import Path

# Listing subdirectories:

p = Path('.')
my_list = [x for x in p.iterdir() if x.is_dir()]
print(my_list)

# Output: 
# [WindowsPath('.vs'), WindowsPath('.vscode'), WindowsPath('00_ALL'), WindowsPath('01_DataCamp_Courses'), WindowsPath('02_linkedIn_Courses'), 
# WindowsPath('04_udemy_Courses'), WindowsPath('05_Other_Courses'), WindowsPath('Challenges'), WindowsPath('How_to_'), WindowsPath('Misc'), 
# WindowsPath('ReadingAndWritingFiles'), WindowsPath('The_Complete_Python_Course_JOSE_SALVATIERRA'), WindowsPath('Web_Scraping'), 
# WindowsPath('Web_Scraping_in_Python'), WindowsPath('Working_with_the_Class_System_in_Python'), WindowsPath('Working_With_Web_Data')]


# Listing Python source files in this directory tree:

list(p.glob('**/*.py'))


# Navigating inside a directory tree:
p = Path('/etc')
q = p / 'init.d' / 'reboot'
print(q) # -> PosixPath('\etc\init.d\reboot')
print(q.resolve()) # -> PosixPath('C:\etc\init.d\reboot')

# Querying path properties:
print(q.exists())
print(q.is_dir())


# Opening a file:
with q.open() as f: f.readline()


