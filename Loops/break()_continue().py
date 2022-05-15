'https://www.programiz.com/python-programming/break-continue'

'''
In Python, break and continue statements can alter the flow of a normal loop.
The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.

If the break statement is inside a nested loop (loop inside another loop), the break statement will terminate the innermost loop.

The continue statement is used to skip the rest of the code inside a loop for the current iteration only. 
Loop does not terminate but continues on with the next iteration.
'''

# Use of break statement inside the loop
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")


# Use of continue statement inside loops
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")


