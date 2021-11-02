from .node import Node
from .bst import BST

class AVL:

  def __init__(self, reverse=False):
    self.bst = BST()
    self.reverse = reverse

  def insert(self, value):
    self.bst.insert(value)

  def delete(self, value):
    pass

  def search(self, value):
    pass

  def traversal(self, order='inorder', start=None):
    self.bst.traversal(order, start)