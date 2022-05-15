'''
While loops are perfect when you repeat an action until a certain condition occurs.

Break will break all the way out of the loop and skip the else clause. 
Continue will shortcut the loop and go back up to the test without finishing the body of the loop, so it won't execute this line 14, 
and else clause only gets executed when the condition is no longer true and the loop exits normally and that'll set auth to true
'''


secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt: 
        break
    if count == 3:
        continue

    pw = input(f"{count}: What's the secret word? ")

else:
    auth = True

print("Authorized" if auth else "Calling the FBI...")
