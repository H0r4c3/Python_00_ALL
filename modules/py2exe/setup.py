'https://www.py2exe.org/index.cgi/Tutorial#Step2'

from distutils.core import setup
import py2exe

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\py2exe\hello_world.py'
path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Controlling_the_Keyboard_and_Mouse\Neverwinter\neverwinter_professions\Mouse_Click_Using_pywinauto_4K.py'
#setup(console=['hello_world.py'])
setup(console=[path])