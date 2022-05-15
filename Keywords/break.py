'https://www.programiz.com/python-programming/break-continue'

'''
The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.

If the break statement is inside a nested loop (loop inside another loop), the break statement will terminate the innermost loop.
'''

# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end!")