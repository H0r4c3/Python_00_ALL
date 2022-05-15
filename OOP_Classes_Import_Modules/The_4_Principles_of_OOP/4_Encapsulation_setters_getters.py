'https://us20.campaign-archive.com/?u=c770c95baa1fa75385fa10ce0&id=8126c65030&e=890e045438'

# without encapsulation
class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def rectangle_area(self):
        return self.base * self.height

new_rectangle = Rectangle(12, 10)
print("Area:", new_rectangle.rectangle_area())


# with encapsulation
class Rectangle:
    def __init__(self, base, height):
        self._base = base
        self._height = height

    def get_base(self):
        return self._base

    def set_base(self, base):
        self._base = base

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def rectangle_area(self):
        return self._base * self._height


my_rectangle = Rectangle(12, 10)
print("Area:", my_rectangle.rectangle_area())

print(my_rectangle.get_base())
my_rectangle.set_base(5)
print(my_rectangle.get_base())

print(my_rectangle.get_height())
my_rectangle.set_height(3)
print(my_rectangle.get_height())

print("New area:", my_rectangle.rectangle_area())  # Expect 15
