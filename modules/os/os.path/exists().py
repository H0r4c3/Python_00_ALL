'https://www.guru99.com/python-check-if-file-exists.html'

'''
Using path.exists you can quickly check that a file or directory exists.
'''

from os import path

def main():

    my_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\os.path\exists().py'
    
    check = path.exists(my_path)
    
    print(f'File exists: {check}')

if __name__== "__main__":
   main()

