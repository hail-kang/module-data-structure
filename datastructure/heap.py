class Heap:
  def __init__(self, elements=[], reverse=False):
    self.elements = elements
    self.reverse = reverse
    self.length = len(elements)

    self.__heapify()

  def __down_heap(self, i):
    left = i*2 + 1
    right = i*2 + 2

    if left < self.length and (self.elements[left] < self.elements[i]) ^ self.reverse:
      priority = left
    else:
      priority = i
    
    if right < self.length and (self.elements[right] < self.elements[i]) ^ self.reverse:
      priority = right

    if priority != i:
      temp = self.elements[priority]
      self.elements[priority] = self.elements[i]
      self.elements[i] = temp

      self.__down_heap(priority)

  def __heapify(self):
    for i in reversed(range(self.length // 2)):
      while i < self.length:
        i_left = 2*i + 1
        i_right = i_left + 1

        if i_left > self.length - 1:
          break
        elif i_right > self.length - 1:
          i_cmp = i_left
        else:
          i_cmp = i_left if (self.elements[i_left] < self.elements[i_right]) ^ self.reverse else i_right

        if (self.elements[i] > self.elements[i_cmp]) ^ self.reverse:
          self.elements[i], self.elements[i_cmp] = self.elements[i_cmp], self.elements[i]

        i = i_cmp

  def push(self, value):
    self.elements.append(value)
    
    i = self.length
    while i > 0:
      i_cmp = (i-1) // 2
      if (self.elements[i] < self.elements[i_cmp]) ^ self.reverse:
        self.elements[i], self.elements[i_cmp] = self.elements[i_cmp], self.elements[i]
      i = i_cmp

    self.length += 1
  
  def pop(self):
    if self.is_empty():
      raise Exception('heap empty')

    self.length -= 1
    value = self.elements[0]
    self.elements[0] = self.elements[self.length]
    self.elements.pop()

    i = 0
    while i < self.length:
      i_left = 2*i + 1
      i_right = i_left + 1

      if i_left > self.length - 1:
        break
      elif i_right > self.length - 1:
        i_cmp = i_left
      else:
        i_cmp = i_left if (self.elements[i_left] < self.elements[i_right]) ^ self.reverse else i_right

      if (self.elements[i] > self.elements[i_cmp]) ^ self.reverse:
        self.elements[i], self.elements[i_cmp] = self.elements[i_cmp], self.elements[i]

      i = i_cmp

    return value

  def is_empty(self):
    return self.length == 0