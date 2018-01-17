'''
# Max. Subarray (Kadane's Algorithm)(need to have 1 pos. number)
# @author: Muhammad Tayyab
# date: 1/16/2018
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
'''

def KadaneAlgo(a):
  last_ending = 0
  max_so_far = 0
  
  for i in range(len(a)):
    last_ending = last_ending+a[i]
    if(last_ending<0):
      last_ending = 0
    if max_so_far <last_ending:
      max_so_far = last_ending
    
  return max_so_far
  



a = [2,-3,4,-1,-2,1,5,-3]
b = KadaneAlgo(a)
print(b)