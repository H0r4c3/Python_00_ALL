
# 1. Method

x={'Alice' : 18}
y={'Bob' : 27, 'Ann' : 22}
z = {**x,**y}

print(z)


# 2. Method (Python 3.9.0 or greater)

book = {"author": "J K Rowling", "book_name": "Harry Potter"}
movie = {"director": "Chris Columbus", "movie_name": "Sorcerers Stone"}

merged_dict = book | movie

print(merged_dict)


# 3. Method

marks = {'Physics':67, 'Maths':87}
internal_marks = {'Practical':48}

marks.update(internal_marks)


print(marks)