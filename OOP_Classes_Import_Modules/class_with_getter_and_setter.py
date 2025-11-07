'''
Why name in __init__? (NOT _name !!!!!!!!!!!!!)

self.name = name in __init__ → validation is always applied.
__init__ uses self.name = name, so it goes through the setter.
Validation happens immediately when you create the object.

If you would have self._name = name in __init__, that would set _name directly, without using the validation!!!!!!!!!!!!!!!!!!!!!!!

You could accidentally create a Person("") without error, because validation is only in the setter!!!!!!!!!!!!!!!!!!!!!!!

Golden rule:
➔ If your setter does only simple assignment, self._name = name is fine in __init__.
➔ If your setter does validation or logic, always use self.name = name in __init__, to apply the same rules at creation.

Why _name in the @property and @setter?

The @property and @name.setter work with that same private variable _name.

The @property is used to get (read) the value of _name.

The @name.setter is used to set (change) the value of _name, but with rules (like checking if it's empty).

Without _name, there would be no place to actually store the value internally.

Simple way to imagine it:

_name = the hidden box inside the object where the name is stored.

name = the nice, public "door" you use to open/close/change that box.

If you didn't have _name, you would cause an infinite loop because the setter and getter would call themselves forever! 😅
(Example of what not to do:)

@property
def name(self):
    return self.name  # WRONG: this calls itself forever
    
That's why we use a different name internally: _name.
'''


class Person:
    def __init__(self, name):
        self.name = name  # Use the setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    def __str__(self):
        return f"Person: {self._name}"


# Example usage
p = Person("Alice")
print(p)         # Output: Person: Alice

p.name = "Bob"
print(p)         # Output: Person: Bob

p.name = ""  # Uncommenting this will raise: ValueError: Name cannot be empty.
