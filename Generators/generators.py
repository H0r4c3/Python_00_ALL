'https://www.youtube.com/watch?v=EnSu9hHGq5o'

'''
Functions return a value
Generators produce a stream

'''

def hello_world():
    yield "Hello"
    yield "World"
    
for x in hello_world():
    print(x)