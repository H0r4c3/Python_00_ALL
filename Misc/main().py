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

