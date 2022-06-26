'https://thepythonguru.com/what-is-if-__name__-__main__/'

'''
Every module in Python has a special attribute called __name__. 
The value of __name__  attribute is set to '__main__'  when module run as main program. 
Otherwise, the value of __name__  is set to contain the name of the module.
'''

import platform

def main():
    test()

def test():
    print(f'This is Python version {platform.python_version()}')

if __name__ == '__main__':
    main()
    
    

'''
https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/#:~:text=Python%20files%20can%20act%20as,run%20directly%2C%20and%20not%20imported

What does the if __name__ == “__main__”: do?

If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”. 
If this file is being imported from another module, __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable.

Every Python module has it’s __name__ defined and if this is ‘__main__’, it implies that the module is being run standalone by the user and 
we can do corresponding appropriate actions.

If you import this script as a module in another script, the __name__ is set to the name of the script/module.

Python files can act as either reusable modules, or as standalone programs.

if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.
'''

