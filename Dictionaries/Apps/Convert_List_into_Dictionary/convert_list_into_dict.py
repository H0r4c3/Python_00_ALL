'''
Convert a file of words into a list of words
Convert the list of words into a dictionary having key = length of words and as value = list of words of that length
'''

from collections import defaultdict

#my_list_of_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
my_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Dictionaries\Apps\Convert_List_into_Dictionary\words.txt'

def read_words_from_file(my_path):
    with open (my_path, 'r') as words:
        line = words.read()
        list_of_words = line.split('\n')
        
        return list_of_words
        

def convert_list_into_dict(list_of_words):
    dict_of_words = defaultdict(list)
    for item in list_of_words:
        dict_of_words[len(item)].append(item)
    
    return dict_of_words


my_list_of_words = read_words_from_file(my_path)
print(my_list_of_words)

my_dict_of_words = convert_list_into_dict(my_list_of_words)
print(my_dict_of_words)