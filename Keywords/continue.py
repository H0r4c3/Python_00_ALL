'https://www.programiz.com/python-programming/break-continue'

'''
The continue statement is used to skip the rest of the code inside a loop for the current iteration only. 
Loop does not terminate but continues on with the next iteration.
'''

# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end!")