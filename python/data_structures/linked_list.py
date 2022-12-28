class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


    def __str__(self):
        return f"{ {self.value} }"


class LinkedList:
    """
   A data structure that contains nodes that links/points to the next node in the list.
    """
    def __init__(self):
        # initialization here
 linked-list-insertions
        self.linked_list = []

        self.head = None

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append("{ " + str(node.value) + " }")
            node = node.next
        if len(values) == 0:
            return "NULL"
        return " -> ".join(values) + " -> NULL"


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


    def append(self, value):
        self.linked_list.append(Node(value))

    def insert_before(self, looking_for, value2):
        old_list = []
        if len(self.linked_list) > 0:
            old_list = self.linked_list
            self.linked_list = []

        for node1 in old_list:
            if node1.value == looking_for:
                self.linked_list.append(Node(value2))
            self.linked_list.append(node1)



    def insert_after(self, looking_for, value2):
        old_list = []
        if len(self.linked_list) > 0:
            old_list = self.linked_list
            self.linked_list = []

        for node1 in old_list:
            self.linked_list.append(node1)
            if node1.value == looking_for:
                self.linked_list.append(Node(value2))
"""
    def to_string(self):
        values = []
        node = self.head
        while node is not None:
            values.append(str(node.value))
            node = node.next
        if len(values) == 0:
            return "NULL"
"""
class TargetError:
    pass
