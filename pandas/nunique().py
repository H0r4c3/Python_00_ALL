'https://www.geeksforgeeks.org/python-pandas-dataframe-nunique/'

'''
Pandas dataframe.nunique() function return Series with number of distinct observations over requested axis. 
If we set the value of axis to be 0, then it finds the total number of unique observations over the index axis. 
If we set the value of axis to be 1, then it find the total number of unique observations over the column axis. 
It also provides the feature to exclude the NaN values from the count of unique numbers.

Syntax: DataFrame.nunique(axis=0, dropna=True)

Parameters :
axis : {0 or ‘index’, 1 or ‘columns’}, default 0
dropna : Don’t include NaN in the counts.

Returns : nunique : Series
'''

# importing pandas as pd
import pandas as pd
  
# Creating the first dataframe 
df = pd.DataFrame({"A":[14, 4, 5, 4, 1],
                   "B":[5, 2, 54, 3, 2],
                   "C":[20, 20, 7, 3, 8],
                    "D":[14, 3, 6, 2, 6]})
  
# Print the dataframe
print(f'{df} \n')

# Let’s use the dataframe.nunique() function to find the unique values across the column axis.\
# As we can see in the output, the function prints the total no. of unique values in each row.
print(df.nunique(axis = 'columns'))


# Across rows
print(df.nunique(axis = 'index'))
