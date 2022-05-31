'https://docs.python.org/3/library/exceptions.html'

'''
Raised by built-in function next() and an iterator's __next__() method to signal that there are no further items produced by the iterator.

The exception object has a single attribute value, which is given as an argument when constructing the exception, and defaults to None.

When a generator or coroutine function returns, a new StopIteration instance is raised, and the value returned by the 
function is used as the value parameter to the constructor of the exception.

If a generator code directly or indirectly raises StopIteration, it is converted into a RuntimeError (retaining the StopIteration as the new exception’s cause).

Changed in version 3.3: Added value attribute and the ability for generator functions to use it to return a value.

Changed in version 3.5: Introduced the RuntimeError transformation via from __future__ import generator_stop, see PEP 479.

Changed in version 3.7: Enable PEP 479 for all code by default: a StopIteration error raised in a generator is transformed into a RuntimeError.
'''

'https://www.w3schools.com/python/gloss_python_iterator_stop.asp'

'''
To prevent the iteration to go on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
'''

#Example
#Stop after 20 iterations:

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)