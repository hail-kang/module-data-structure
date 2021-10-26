from .node import Node

class BST:

  def __init__(self, reverse=False):
    self.root = None
    self.reverse = reverse

  def insert(self, value):
    if self.root == None:
      self.root = Node(value)
    else:
      next_node = self.root
      while next_node != None:
        node = next_node
        if value < node.value:
          next_node = node.left
        else:
          next_node = node.right

      if value < node.value:
        node.left = Node(value)
      else:
        node.right = Node(value)
      

  def remove(self, value):
    pass

  def search(self, value):
    pass