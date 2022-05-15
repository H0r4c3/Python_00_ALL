'''
Created on Oct 18, 2020

@author: Horace.000
'''

fam = [1.73, 1.68, 1.71, 1.89]

for i in fam:
    print(i)

# enumerate creates a list of tuples of index and value
for e in enumerate(fam):    
    print(e)
    
    
for index, value in enumerate(fam):
    print("index:" + str(index) + " -- " + "value:" + str(value))