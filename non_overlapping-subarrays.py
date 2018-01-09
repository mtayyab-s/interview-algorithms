'''
Given an array of N elements, you are required to find the maximum sum of lengths of all non-overlapping subarrays with K as the maximum element in the subarray.
http://practice.geeksforgeeks.org/problems/sum-of-lengths-of-non-overlapping-subarrays/0
'''

T= int(input())
for p in range(T):
    N =int(input())
    arr  = [int(i) for i in input().split()]
    k = int(input())
    lis=[]
    count =0
    i=0
    while i<len(arr):
        temp=[]
        j=i
        while j<len(arr) :
            if arr[j]<=k:
                temp.append(arr[j])
                j=j+1
            else:
                break
        lis.append(temp)
        i=j+1

    for i in lis:
        if k in i:
            count=count+len(i)
    print(count)