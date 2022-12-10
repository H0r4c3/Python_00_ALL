'https://docs.python.org/3/library/os.html'

'''
os.startfile(path[, operation][, arguments][, cwd][, show_cmd])
Start a file with its associated application.

When operation is not specified or 'open', this acts like double-clicking the file in Windows Explorer, 
or giving the file name as an argument to the start command from the interactive command shell: the file 
is opened with whatever application (if any) its extension is associated.


https://python101.pythonlibrary.org/chapter16_os.html

The os.startfile() method allows us to “start” a file with its associated program. 
In other words, we can open a file with it’s associated program, just like when you double-click a PDF and it opens in Adobe Reader. 

'''

import os

path = r'c:\test_file.txt'
try:
    os.startfile(path)
except FileNotFoundError as f:
    print(f)
    print('No file found! Select the correct path for the file!')