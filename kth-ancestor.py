'''
# https://www.geeksforgeeks.org/kth-ancestor-node-binary-tree/
# K-th ancestor of a node in Binary Tree
# Muhammad Tayyab
# 1/10/2018
'''

from collections import deque

class Node:
  def __init__(self,value):
    self.left = None
    self.right = None
    self.data = value
    
  def findAncestor(self,root,dat,k):
    queue = deque([root])
    bfs = []
    index = [-1]
    i=0
    ancestor = None
    while(queue):
      temp = queue.popleft()
      bfs.append(temp.data)
      if temp.data==dat:
        break
      if(temp.left):
        queue.append(temp.left)
        index.append(i)
      if(temp.right):
         queue.append(temp.right)
         index.append(i)
      i=i+1
    
    
    id = index[len(bfs)-1]
  
    while(k!=0):
      if id==-1:
        ancestor =-1
        break
      ancestor = bfs[id]
      id = index[id]
      k=k-1
    print(ancestor)
      
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.findAncestor(root,3,2)


