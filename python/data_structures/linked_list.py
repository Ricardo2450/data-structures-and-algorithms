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

        self.linked_list = []

        self.head = None
        self.counter = 0

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
        self.counter += 1


    def includes(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
            self.counter += 1
        return False


    def append(self, value):
        self.linked_list.append(Node(value))
        self.counter += 1


    def insert_before(self, looking_for, value2):
        old_list = []
        if len(self.linked_list) > 0:
            old_list = self.linked_list
            self.linked_list = []

        for node1 in old_list:
            if node1.value == looking_for:
                self.linked_list.append(Node(value2))
            self.linked_list.append(node1)

            self.counter += 1


    def insert_after(self, looking_for, value2):
        old_list = []
        if len(self.linked_list) > 0:
            old_list = self.linked_list
            self.linked_list = []

        for node1 in old_list:
            self.linked_list.append(node1)
            if node1.value == looking_for:
                self.linked_list.append(Node(value2))

                self.counter += 1

    def kth_from_end(self, k):
        new_list = []
        current = self.head
        while current:
            new_list.append(current.value)
            current = current.next
        if k > len(new_list):
            raise TargetError
        else:
            return new_list[-k - 1]




class TargetError:
    pass
