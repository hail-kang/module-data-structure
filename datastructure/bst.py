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

  def delete(self, value):
    node = self.search(value)
    if node == None:
      raise Exception("Can't find value")

    while node != None:
      if node.right == None:
        if node.left == None:
          break
        else:
          node.value = node.left.value
          node = node.left
      else:
        node.value = node.right.value
        node = node.right

  def search(self, value):
      next_node = self.root
      while next_node != None:
        node = next_node
        if value == node.value:
          return node
        elif value < node.value:
          next_node = node.left
        else:
          next_node = node.right
      return None


