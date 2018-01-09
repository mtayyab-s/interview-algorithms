'''
Given a sorted array consisting 0’s and 1’s. The task is to find the index of first ‘1’ in the sorted array.

'''

T=int(input())
for i in range(T):
    n =int(input())
    arr= [int(i) for i in input().split()]
    b=1
    ans=-1
    
    n = len(arr)
    start=0
    end=n-1
    while(start<=end):
        mid = int((start+end)/2)
        if arr[start==b] and start==0:
            ans=0
            break
        elif arr[mid]==b and arr[mid-1]==0:
            ans = mid

            break
        elif arr[mid]==1 and arr[mid-1]==1:
            end = mid-1
        elif arr[mid]==0:
            start=mid+1


    print(ans)