from .node import Node

class AVL:

  def __init__(self, reverse=False):
    self.root = None
    self.reverse = reverse

  def insert(self, value):
    if self.root == None:
      self.root = Node(value)

  def delete(self, value):
    pass

  def search(self, value):
    pass

  def __depth(self, node):
    pass