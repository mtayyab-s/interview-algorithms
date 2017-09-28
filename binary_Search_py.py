def bSearch(start,end,A,num):
    mid = int((start+end)/2)
    print("mid: ",mid)
    if start>end:
        return -1
    if A[mid]==num:
        print("ans: ",mid)
        return mid
    elif A[mid]>num:
        return bSearch(start,mid-1,A,num)
    elif A[mid]<num:
        return bSearch(mid+1,end,A,num)
    
        
A= [1,5,9,10,12,13,17]
ans = bSearch(0,len(A)-1,A,5)
print(ans)