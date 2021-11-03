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
        node.left = Node(value, None, None, node)
      else:
        node.right = Node(value, None, None, node)

  def delete(self, value):
    node = self.root
    if node == None:
      raise Exception("Empty Error")

    parent_node = node
    while node != None:
      if value == node.value:
        break
      elif (value < node.value) ^ self.reverse:
        parent_node = node
        node = node.left
      else:
        parent_node = node
        node = node.right

    if node == None:
      raise Exception("Can't find value")
    
    if node.left == None and node.right == None:
      if parent_node.left == node:
        parent_node.left = None
      else:
        parent_node.right = None
    elif node.left != None and node.right == None:
      if parent_node.left == node:
        parent_node.left = node.left
      else:
        parent_node.right = node.left
    elif node.left == None and node.right != None:
      if parent_node.left == node:
        parent_node.left = node.right
      else:
        parent_node.right = node.right
    else:
      parent_temp = node
      temp = node.left
      while temp.right != None:
        parent_temp = temp
        temp = temp.right
      if temp.left == None:
        node.value = temp.value
        parent_temp.right = None
      else:
        node.value = temp.value
        temp.value = temp.left.value
        temp.left = None

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
