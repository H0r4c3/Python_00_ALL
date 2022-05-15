'https://www.youtube.com/watch?v=EnSu9hHGq5o'

'''

Iterable: produces an iterator # iterable.__iter__() 
Iterables = LIST, STRING, TUPLE

Iterator: produces a stream of values # iterator.next() or .__next__()
Iterators = zip()...

iterator = iter(iterable)

value = next(iterator)
value = next(iterator)
...

Only operation on iterators is next().

'''

my_list = [1, 2, 3]
my_list2 = ['a', 'b', 'c']

iterator = iter(my_list)
print(next(iterator))

zipper = zip(my_list, my_list2)
print(next(zipper))




'https://www.geeksforgeeks.org/python-difference-iterable-iterator/'

# list of cities
cities = ["Berlin", "Vienna", "Zurich"]
  
# initialize the object
iterator_obj = iter(cities)
  
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
