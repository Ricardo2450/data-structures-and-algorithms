class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def post_order(self, root=None, nodes=None):
        """
        Return a list of nodes in a BT, in post order
        eg: [4, 5, 2, 6, 7, 3, 1]
        """
        # start at the root of our tree
        if root is None:
            root = self.root

        if nodes is None:
            nodes = []

        # Left child
        if root.left:
            self.post_order(root.left, nodes)

        # Right child
        if root.right:
            self.post_order(root.right, nodes)

        # Root
        nodes.append(root.value)

        return nodes
        # print(root.value)

    def pre_order(self, root=None, nodes=None):
        """
        Return a list of nodes in a BT, in pre order
        eg: [1, 2, 4, 5, 3, 6, 7]
        """
        if nodes is None:
            nodes = []

        if root is None:
            root = self.root

        # Root
        nodes.append(root.value)

        #return nodes
        # print(root.value)

        # Left child
        if root.left:
            self.pre_order(root.left, nodes)

        # Right child
        if root.right:
            self.pre_order(root.right, nodes)

        return nodes

    def in_order(self, root=None, nodes=None):
        """
        Return a list of nodes in a BT, in in order
        eg: [4, 2, 5, 1, 6, 3, 7]
        """
        if nodes is None:
            nodes = []

        if root is None:
            root = self.root

        # Left child
        if root.left:
            self.in_order(root.left, nodes)

        # Root
        nodes.append(root.value)
        # print(root.value)


        # Right child
        if root.right:
            self.in_order(root.right, nodes)

        return nodes


