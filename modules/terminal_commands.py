'Run in terminal the following commands:'

# Check all installed Python packages with pip list / pip freeze
'pip freeze'
'pip list'
'List uptodate packages: pip freeze uptodated'
'List outdated packages: pip freeze outdated'
'pip freeze > requirements.txt'


'''
Updating Python Packages:

1. Output a list of installed packages into a requirements file (requirements.txt): 
pip freeze > requirements.txt

2. Edit requirements.txt, and replace all ‘==’ with ‘>=’. Use the ‘Replace All’ command in the editor.

3. Restore the packages to another environment
pip install -r requirements.txt

4. Upgrade all outdated packages: 
pip install -r requirements.txt --upgrade

pip install -U -r requirements.txt

5. Upgrade a package
pip install --upgrade tkinter

6. Install a package without PIP
Download the package.
unzip it if it is zipped.
cd into the directory containing setup.py.
If there are any installation instructions contained in documentation contianed herein, read and follow the instructions OTHERWISE.
type in python setup.py install.

7. Where is pip cache folder
pip cache dir

'''

# Install pip
'''
https://www.geeksforgeeks.org/how-to-install-pip-on-windows/

Download the get-pip.py file and store it in the same directory as python is installed
Change the current path of the directory in the command line to the path of the directory where the above file exists.
Run the command given below:
python get-pip.py
and wait through the installation process.

'''