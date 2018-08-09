""" Linked List implementation in Python. Sinlgy and Doubly Linked.
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self, head):
    self.head = head


class DoublyNode:
    def __init__(self, val):
      self.val = val
      self.next = None
      self.prev = None
