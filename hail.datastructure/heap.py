from .leaf import Leaf

class Heap:
  def __init__(self, elements=[], reverse=False):
    self.elements = elements
    self.reverse = reverse
    self.length = len(elements)

  def add(self, value):
    self.elements.append(value)
    
    i = self.length
    while i > 0:
      cmp_i = (i-1) // 2
      if (self.elements[i] < self.elements[cmp_i]) ^ self.reverse:
        self.elements[i], self.elements[cmp_i] = self.elements[cmp_i], self.elements[i]
      i = cmp_i

    self.length += 1

