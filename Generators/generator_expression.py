'https://realpython.com/introduction-to-python-generators/'

'''
A common use case of generators is to work with data streams or large files, like CSV files.
You can define a generator expression (also called a generator comprehension), which has a very similar syntax to list comprehensions. 
In this way, you can use the generator without calling a function:
'''

# csv_gen = (row for row in open(file_name)) <- same as list comprehension, but with round parentheses

# In this version, you open the file, iterate through it, and yield a row. 
# This code should produce the output, without memory errors:
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row