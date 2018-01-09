'''
Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value.
Note: Expected time complexity O(n^2).
http://practice.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x/0

'''

T = int(input())
for i in range(T):
    n,sum=(input().split())
    n=int(n)
    sum = int(sum)
    arr= [int(i) for i in input().split()] 
    count=0

    n=len(arr)
    arr = sorted(arr)

    for i in range(n-2):
        j=i+1
        k=n-1
        while(j<k):
            if arr[i]+arr[j]+arr[k]>=sum:
                k=k-1
            else:
                count=count+(k-j)
                j=j+1

    print(count)