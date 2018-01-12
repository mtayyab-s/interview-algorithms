'''
# https://www.geeksforgeeks.org/foldable-binary-trees/
# Foldable Binary Trees
# @author: Muhammad Tayyab
# 1/12/2018
'''

class Node    
  def __init__(self,value):
    self.left = None
    self.right = None
    self.data = value
    
def isFoldable(root):
  if root ==None:
    return True
  mirror(root.left)
  
  res = isStructSame(root.left,root.right)
  
  mirror(root.left)
  
  return res
    
def isStructSame(left,right):
  if left==None and right == None:
    return True
  if left!=None and right!=None and isStructSame(left.left,right.left) and isStructSame(left.right,right.right):
    return True
  return False
  
def mirror(node):
  if node==None:
    return
  else:
    mirror(node.left)
    mirror(node.right)
    
    temp = node.left
    node.left = node.right
    node.right = temp
    

root = Node(10)
root.left = Node(7)
root.right = Node(15)
root.left.left = Node(5)
root.right.left = Node(11)

if isFoldable(root)==True:
  print("yes")
else:
  print("no")


