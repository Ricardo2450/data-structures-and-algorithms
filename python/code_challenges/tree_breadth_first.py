from data_structures.binary_tree import BinaryTree


def breadth_first(tree):
    try:
        result = []
        queue = [tree.root]
        while queue:
            front = queue.pop(0)
            result.append(front.value)
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
        return result
    except:
        return []
