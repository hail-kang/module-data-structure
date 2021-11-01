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

  def traversal(self, order='inorder', start=None):
    if start == None:
      node = self.root
    else:
      node = start
    
    if order == 'preorder':
      print(node.value)
      if node.left != None:
        self.traversal(order, node.left)
      if node.right != None:
        self.traversal(order, node.right)
    elif order == 'inorder':
      if node.left != None:
        self.traversal(order, node.left)
      print(node.value)
      if node.right != None:
        self.traversal(order, node.right)
    elif order == 'postorder':
      if node.left != None:
        self.traversal(order, node.left)
      if node.right != None:
        self.traversal(order, node.right)
      print(node.value)

  def __depth(self, node):
    pass