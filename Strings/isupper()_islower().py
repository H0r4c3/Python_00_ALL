'https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/'

my_string = 'GeeksforGeeks'

counter = 0
for item in my_string:
    if item.isupper():
        counter += 1
        
print(f'There are {counter} Upper Cases')