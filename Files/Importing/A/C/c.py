# In C/c.py

'''
A/
├── __init__.py
├── a.py
├── B/
│   ├── __init__.py
│   └── b.py
└── C/
    ├── __init__.py
    └── c.py

# Import from parent folder A
from ..a import function_from_a  # or: from .. import a

# Import from sibling folder B
from ..B.b import function_from_b  # or: from ..B import b

# Import from parent and sibling folders
from ..a import function_from_a
from ..B.b import function_from_b
'''

from A import a
from A.B import b

def function_from_c():
    print("Hello from script c!")
    
    # Test the imports
    result_a = a.function_from_a()
    result_b = b.function_from_b()
    
    print(f"Got: {result_a} and {result_b}")

def main():
    print("Running c.py")
    function_from_c()

if __name__ == "__main__":
    main()