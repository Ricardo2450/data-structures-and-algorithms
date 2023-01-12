from data_structures.binary_tree import BinaryTree

class Node:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children


def fizz_buzz_tree(root):
    if not root:
        return None

    if root.value % 15 == 0:
        new_value = "FizzBuzz"

    elif root.value % 5 == 0:
        new_value = "Buzz"

    elif root.value % 3 == 0:
        new_value = "Fizz"

    else:
        new_value = str(root.value)

    new_children = [fizz_buzz_tree(child) for child in root.children]

    return Node(new_value, new_children)
