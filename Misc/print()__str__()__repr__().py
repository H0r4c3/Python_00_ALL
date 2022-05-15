import platform

# 1. Example
print('This is Python version {}' .format(platform.python_version()))

# 2. Example
print(f'This is Python version {platform.python_version()}')


# 3. Example
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
     
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"title={self.title}, author={self.author}"

my_book = Book("War and Peace", "Leo Tolstoy")

print(my_book)
print(repr(my_book))



# 4. Example
numbers = [2, 1, 3, 4, 7]
print(*numbers, sep='H')

