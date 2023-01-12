from data_structures.invalid_operation_error import InvalidOperationError

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


class Queue:
  """
  Docstring here
  """

  def __init__(self):
    self.front = None
    self.rear = None
"""
  def enqueue(self, value):
  # checks to see if queue is empty
    if self.rear:
      self.rear.next = Node(value)
      self.rear = self.rear.next
      return
    self.rear = self.front = Node(value)
"""

  def enqueue(self, value):
      new_node = Node(value)
      if self.head is None:
          self.head = new_node

  if self.tail:
      self.tail.next = new_node
      self.tail = new_node
  else:
      self.tail = new_node

  def dequeue(self):
      if self.front is None:
          raise InvalidOperationError
      elif self.front:
        dequeued = self.front
        self.front = self.front.next
        return dequeued.value

  def peek(self):
      if self.front is None:
          raise InvalidOperationError("Method not allowed on empty collection")
      elif self.front:
        popped = self.front
        self.front = self.front.next
        return popped.value


  def is_empty(self):
      if self.front is None:
          return True
      else:
          return False
