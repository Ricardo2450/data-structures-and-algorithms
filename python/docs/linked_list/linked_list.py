class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
   A data structure that contains nodes that links/points to the next node in the list.
    """

    def __init__(self):
        # initialization here
        self.head = None


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


    def to_string(self):
        values = []
        node = self.head
        while node is not None:
            values.append(str(node.value))
            node = node.next
        if len(values) == 0:
            return "NULL"



class TargetError:
    pass
