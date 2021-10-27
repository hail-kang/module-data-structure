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
        if (value < node.value) ^ self.reverse:
          next_node = node.left
        else:
          next_node = node.right

      if (value < node.value) ^ self.reverse:
        node.left = Node(value)
      else:
        node.right = Node(value)

  def delete(self, value):
    node = self.search(value)
    if node == None:
      raise Exception("Can't find value")

    next_node = node
    while next_node.left != None or next_node.right != None:
      node = next_node
      if next_node.right != None:
        next_node.value = next_node.right.value
        next_node = next_node.right
      else:
        next_node.value = node.left.value
        next_node = next_node.left
      
    if self.root == next_node:
      self.root = None
    elif node.left == next_node:
      node.left = None
    else:
      node.right = None

  def search(self, value):
      next_node = self.root
      while next_node != None:
        node = next_node
        if value == node.value:
          return node
        elif (value < node.value) ^ self.reverse:
          next_node = node.left
        else:
          next_node = node.right
      return None

  def traversal(self, order='preorder', start=None):
    if start == None:
      node = self.root
    else:
      node = start
    
    if order == 'preorder':
      if node.left != None:
        self.traversal(order, node.left)
      print(node.value)
      if node.right != None:
        self.traversal(order, node.right)
    elif order == 'inorder':
      print(node.value)
      if node.left != None:
        self.traversal(order, node.left)
      if node.right != None:
        self.traversal(order, node.right)
    elif order == 'postorder':
      if node.left != None:
        self.traversal(order, node.left)
      if node.right != None:
        self.traversal(order, node.right)
      print(node.value)
