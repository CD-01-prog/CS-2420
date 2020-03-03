class Node:
    def __init__(self, val):
        self.val = val
        self.mleft = None
        self.mright = None
    
    def get(self):
        return self.val
    
    def set(self, val):
        self.val = val
        
    def getChildren(self):
        children = []
        if(self.mleft != None):
            children.append(self.mleft)
        if(self.mright != None):
            children.append(self.mright)
        return children

class UUC:

  def __init__(self):
    self.root = None

  def setRoot(self, val):
    self.root = Node(val)

  def get(self):
    return self.Node
  
  def name(self,name):
    self.Node = name

  #only usefull for this assignment
  def Findssn(self,student):
    student = student.split()
    bits = student[2]
    return bits

  #if given node.val converts it into the age
  def collectage(self,student):
    student = student.split()
    age = student[4]
    return float(age)

  #check to see if exist
  def exist(self,item):
    current = self.root
    while current is not None:
      if self.Findssn(current.val) == item:
	      return True
      elif item < self.Findssn(current.val):
        current = current.mleft
      else:
        current = current.mright
    return False
  
  #insert into a list
  def insert(self, val):
    if self.root is None:
      self.setRoot(val)
    else:
      self.insertR(self.root, val)
  def insertR(self, current, val):
    if(self.Findssn(val) < self.Findssn(current.val)):
      if(current.mleft):
        self.insertR(current.mleft, val)
      else:
        current.mleft = Node(val)
    elif(self.Findssn(val) > self.Findssn(current.val)):
      if(current.mright):
        self.insertR(current.mright, val)
      else:
        current.mright = Node(val)
    else:
      return False
  
  #go over a list doing a function
  def Traverse(self,function):
    self.transversR(self.root,function)
    return
  def transversR(self,current,function):
    if current is None:
      return
    function(current.val)
    self.transversR(current.mleft,function)
    self.transversR(current.mright,function)

  #delete a item from a list
  def Delete(self,remove):
    if not self.exist(remove):
      return False
    self.deleteR(remove,self.root)
    return True
  def deleteR(self,item,current):
    if item < self.Findssn(current.val):
      self.root = self.deleteR(item,current.mleft)
    elif item > self.Findssn(current.val):
      self.root = self.deleteR(item,current.mright)
    else:
      if current.mleft == None and current.mright == None:
        current = None
      elif current.mleft == None:
        current = current.mright
      elif current.mright == None:
        current = current.mleft  
      else:
        succesor = current.mright
        while succesor.mleft:
          succesor = succesor.mleft
        current.mitem = succesor.val
        self.deleteR(self.Findssn(succesor.val),current.mright)
    return current

  #retrive specific items from a list
  def retrive(self,item):
    if not self.exist(item):
      return False
    return self.retriveR(item,self.mRoot)
  def retriveR(self,item,current):
    if current is None:
      return None
    elif self.Findssn(current.item) == item:
      return current.item
    elif item < self.Findssn(current.item):
      return self.reteriveR(self,item,current.mleft)
    elif item > self.Findssn(current.item):
      return self.reteriveR(self,item,current.mright)

  #get the size of the list
  def size(self):
    return self.sizeR(self.root)
  def sizeR(self,current):
    if current is None:
      return 0
    return 1 + self.sizeR(current.mleft) + self.sizeR(current.mright)

  def AgeR(self,current):
    age = self.collectage(current.val)
    self.AgeR(current.mleft)
    self.AgeR(current.mright)
    return age



  

  """correct answer
  class Node:
    def __init__(self, val):
        self.val = val
        self.mleft = None
        self.mright = None
    
    def get(self):
        return self.val
    
    def set(self, val):
        self.val = val
        
    def getChildren(self):
        children = []
        if(self.mleft != None):
            children.append(self.mleft)
        if(self.mright != None):
            children.append(self.mright)
        return children
        
class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.mleft):
                self.insertNode(currentNode.mleft, val)
            else:
                currentNode.mleft = Node(val)
        elif(val > currentNode.val):
            if(currentNode.mright):
                self.insertNode(currentNode.mright, val)
            else:
                currentNode.mright = Node(val)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if(currentNode is None):
            return False
        elif(val == currentNode.val):
            return True
        elif(val < currentNode.val):
            return self.findNode(currentNode.mleft, val)
        else:
            return self.findNode(currentNode.mright, val)
"""
