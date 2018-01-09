'''
# ZigZag Tree Traversal
# https://www.geeksforgeeks.org/zigzag-tree-traversal/
# Muhammad Tayyab
# 01/09/2018
'''


class Node:
  def __init__(self,value):
    self.left = None
    self.right = None
    self.data = value
  
  def display(self,root):
    #pre-order traversal
    
    rightToLeft = True
    currentLevel = []
    nextLevel = []
    currentLevel.append(root)
    while(currentLevel):
      temp = currentLevel.pop()
      if(temp):
        print(temp.data)
        if(rightToLeft==True):
          if(temp.left!=None):
            nextLevel.append(temp.left)
          if(temp.right!=None):
            nextLevel.append(temp.right)
        else:
          if(temp.right!=None):
            nextLevel.append(temp.right)
          if(temp.left!=None):
            nextLevel.append(temp.left)
      if not currentLevel:
        tem = currentLevel
        currentLevel = nextLevel
        nextLevel = tem
        rightToLeft = not rightToLeft
        
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
root.display(root)

