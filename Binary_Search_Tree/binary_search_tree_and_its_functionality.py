'https://www.learnsteps.com/binary-search-tree-functionality-python/'

'''
Node class to make the nodes of binary search tree.

Then insert functions, what this function is doing is checking if the data is lesser than node then 
moves to left child else moves to right child and place it at the end.

Search function again works same as insert functions. The only difference is in this we are getting and telling if 
the data is present while in insert we are adding node to the true.

In order traversal to visit all the node. Do you know in order traversal of binary search tree is in sorted order.

Get min and Get max functions to get the minimum and maximum of the Binary Search Tree.
'''

class Node():
    def __init__(self,data):
      self.left = None
      self.right = None
      self.data = data


def insert(root, data):
    if root.data > data:
        if root.left:
            insert(root.left,data)
        else:
            tmp = Node(data)
            root.left = tmp
    elif root.data < data:
        if root.right:
            insert(root.right,data)
        else:
            tmp = Node(data)
            root.right = tmp
    else:
        print("Key already exist")


def in_order(root):
    if root:
        in_order(root.left)
        print(root.data)
        in_order(root.right)


def search(root,key):
    if root:
        if root.data == key:
            return True
        elif root.data < key:
            return search(root.right, key)
        else:
            return search(root.left, key)
    return False 


def get_min(root):
    while root.left:
        root = root.left
    return root.data


def get_max(root):
    while root.right:
        root = root.right
    return root.data


a = Node(4)
insert(a,2)
insert(a,5)
insert(a,1)
insert(a,3)
insert(a,8)
in_order(a)


print(search(a,8))
print(search(a,2))
print(search(a,23))
print(get_max(a))
print(get_min(a))