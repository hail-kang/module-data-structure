class Node:

  def __init__(self, value, left=None, right=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent
  
  def getDepth(self):
    if self.left == None and self.right == None:
      return 0
    elif self.left != None and self.right == None:
      return self.left.depth()
    elif self.left == None and self.right != None:
      return self.right.depth()
    else:
      return max(self.left.depth(), self.right.depth())
    
  def getBalanceFactor(self):
    if self.left == None and self.right == None:
      return 0
    elif self.left != None and self.right == None:
      return self.left.depth()
    elif self.left == None and self.right != None:
      return -self.right.depth()
    else:
      return self.left.depth() - self.right.depth()
      
