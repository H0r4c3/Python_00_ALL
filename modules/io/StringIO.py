'https://docs.python.org/3/library/io.html'

'''
The io module provides Python’s main facilities for dealing with various types of I/O.

In-memory text streams are also available as StringIO objects:

f = io.StringIO("some initial text data")
'''

from io import StringIO

# Create a StringIO object
string_buffer = StringIO()

# Write some text to the buffer
string_buffer.write("Hello, world!")

# Get the value of the buffer as a string
buffer_contents = string_buffer.getvalue()

# Print the contents of the buffer
print(buffer_contents)

# Close the buffer
string_buffer.close()