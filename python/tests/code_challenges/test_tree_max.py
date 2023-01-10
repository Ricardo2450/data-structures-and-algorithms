from data_structures.binary_tree import BinaryTree, Node

def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_max_val_empty():
    tree = BinaryTree()
    actual = tree.find_maximum_value()
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_max_val_larger_tree():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(45)
    tree.root.right = Node(21)
    tree.root.left.left = Node(9.6)
    tree.root.left.right = Node(100.1)
    tree.root.right.left = Node(2)
    tree.root.right.right = Node(-67)
    actual = tree.find_maximum_value()
    expected = 100.1
    assert actual == expected
