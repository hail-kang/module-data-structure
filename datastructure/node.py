class Node:

  def __init__(self, value, left=None, right=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent
  
  def get_depth(self):
    if self.left == None and self.right == None:
      return 0
    elif self.left != None and self.right == None:
      return self.left.get_depth()
    elif self.left == None and self.right != None:
      return self.right.get_depth()
    else:
      return max(self.left.get_depth(), self.right.get_depth())
    
  def get_balance_factor(self):
    if self.left == None and self.right == None:
      return 0
    elif self.left != None and self.right == None:
      return self.left.get_depth()
    elif self.left == None and self.right != None:
      return -self.right.get_depth()
    else:
      return self.left.get_depth() - self.right.get_depth()
      
