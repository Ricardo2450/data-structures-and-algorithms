from python.data_structures.binary_tree import BinaryTree


def tree_intersection(tree_1, tree_2):
    dict = {}

    if not tree_1.root or not tree_2.root:
        return None

    def helper(root):
        nonlocal dict
        if root.left:
            helper(root.left)
        if root.right:
            helper(root.right)

        if dict[root.value]:
            dict[root.value] += 1
        else:
            dict[root.value] = 1

    for tree in [tree_1, tree_2]:
        helper(tree.root)

    if dict:
        return [key for key, value in dict if value > 1]
    else:
        return None
