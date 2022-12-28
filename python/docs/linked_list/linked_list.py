class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
   A data structure that contains nodes that links/points to the next node in the list.
    """

    def __init__(self, head=None):
        # initialization here
        self.head = head

    def __str__(self):
        return "NULL"

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def includes(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False





class TargetError:
    pass
