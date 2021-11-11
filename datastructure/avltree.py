from .node import Node
from .bst import BST

from collections import deque

class AVL:

  def __init__(self, reverse=False):
    self.bst = BST()
    self.reverse = reverse

  def insert(self, value):
    self.bst.insert(value)
    self.__balancing()

  def delete(self, value):
    self.bst.delete(value)
    self.__balancing()

  def search(self, value):
    return self.bst.search(value)

  def traversal(self, order='inorder', start=None):
    self.bst.traversal(order, start)

  def __balancing(self):
    deq = deque([self.bst.root])
    x = y = z = None
    while len(deq) > 0:
      node = deq.popleft()
      if node.get_balance_factor() > 1:
        z = node
        break
      if node.left != None:
        deq.append(node.left)
      if node.right != None:
        deq.append(node.right)
    
    if z != None:
      if z.left == None and z.right == None:
        pass
      elif z.left != None and z.right == None:
        y = z.left
      elif z.left == None and z.right != None:
        y = z.right
      else:
        left_depth = z.left.get_depth()
        right_depth = z.right.get_depth()
        if left_depth < right_depth:
          y = z.right
        else:
          y = z.left

    if y != None:
      if y.left == None and y.right == None:
        pass
      elif y.left != None and y.right == None:
        x = y.left
      elif y.left == None and y.right != None:
        x = y.right
      else:
        left_depth = y.left.get_depth()
        right_depth = y.right.get_depth()
        if left_depth < right_depth:
          x = y.right
        else:
          x = y.left 

    if x != None:
      a = b = c = None
      T0 = T1 = T2 = T3 = None
      if z.left == y:
        c = z
        T3 = z.right
        if y.left == x:
          b = y
          T2 = y.right

          a = x
          T1 = x.right
          T0 = x.left
        else:
          b = x
          T2 = x.right
          T1 = x.left

          a = y
          T0 = y.left
      else:
        a = z
        T0 = z.left
        if y.left == x:
          b = x
          T1 = x.left
          T2 = x.right

          c = y
          T3 = y.right
        else:
          b = y
          T1 = y.left

          c = x
          T2 = x.left
          T3 = x.right

      p = z.parent

      b.parent = p
      b.left = a
      b.right = c

      a.parent = c.parent = b
      a.left = T0
      a.right = T1
      b.left = T2
      b.right = T3