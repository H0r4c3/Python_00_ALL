'''
Created on Dec 22, 2020

@author: Horace.000
'''
'https://learning.oreilly.com/scenarios/getting-started-with/9781492085485/'

import pandas as pd

df = pd.DataFrame({'City' : ['New York', 'London', 'Paris', 'Istanbul'],'Population (million)':  [8399, 8982, 2143, 1552], })

print("DataFrame:")
print(df.head()) # returns the first n rows (default=5)
print(df)

data = pd.Series([15,'hello',25,'apple','23.3'])

print("\nSeries: ")
print(data)