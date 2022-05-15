'https://www.jcchouinard.com/generate-dummy-data-with-python/'

# Create DataFrame

import pandas as pd
pd.util.testing.makeDataFrame().head()

# or

import pandas as pd
 
s = pd.Series(list('abca'))
pd.get_dummies(s)


# Create a List of Dictionaries

from random import randint
 
num_list = 5
num_keys = 3
 
list_of_dicts = []
 
for i in range(num_list):
    d = {}
    for j in range(1,num_keys+1):
        d[chr(j+96)]=randint(1,10)
    list_of_dicts.append(d)

print(list_of_dicts)


# Create a Dictionary of Lists

from random import randint
 
num_keys = 5
letters = []
for i in range(1,num_keys+1):
    letters.append(chr(i+96))
 
dict_of_lists = {key: list(range(randint(5,10))) for key in letters}

print(dict_of_lists)

# Create DataFrame from Lists

def make_df_from_lists(index,**kwargs):
    return pd.DataFrame(list(zip(*kwargs.values())),index=index,columns=list(kwargs.keys()))
 
index = ['United States', 'Germany', 'Great Britain', 'Russia', 'China', 'France', 'Australia', 'Italy', 'Canada', 'Japan']
 
gold = [137, 47, 64, 50, 44, 20, 23, 8, 4, 17]
silver = [52, 43, 55, 28, 30, 55, 34, 38, 4, 13]
bronze = [67, 67, 26, 35, 35, 21, 25, 24, 61, 34]
 
make_df_from_lists(index,Bronze=bronze,Gold=gold,Silver=silver)
