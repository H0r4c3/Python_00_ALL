'''
Convert a file with words separated by spaces into a file with a word in every line
'''

'''
https://theprogrammingexpert.com/python-difference-between-read-readline-readlines/?utm_content=cmp-true
read() reads the entire file and returns a string
readline() reads just one line from a file
readlines() returns a list of strings representing the lines of the file

https://net-informations.com/python/file/diff.htm
The read method reads the entire content of a file and returns it as a string.
The readline method reads a single line from a file and returns it as a string.
The readlines method reads the entire content of a file and returns it as a list of strings, 
where each element of the list is a single line of the file.
'''

path_1 = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\GUI\Crosswords\DEX_REBUS.txt'
path_2 = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\GUI\Crosswords\DEX_REBUS_LINES.txt'
total = 0

with open (path_1, 'r', encoding='UTF-8') as open_file:
    content = open_file.read()
    #print(f'content = {content}')

content_splitted = content.split()
#print(f'content_splitted = {content_splitted}')
    
with open (path_2, 'w', encoding='UTF-8') as write_file:
    for item in content_splitted:
        write_file.write(item + '\n')
        total += 1

print(f'Finished transferring of {total} words!')


        

