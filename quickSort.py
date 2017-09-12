'''
Quicksort average case O(nlogn), worst cas O(n^2)
'''

partition(start,end,A):
    pIndex = start
    pivot = A[end]
    for i in range(start,end):
        if A[i]<=pivot:
            A[i],A[pIndex] = A[pIndex],A[i]
            pIndex = pIndex+1
    A[end],A[pIndex] = A[pIndex],A[end]
    
    return pIndex


def quickSort(start,end,A):
    if start<end:
        pIndex = partition(start,end,A)
        quickSort(start,pIndex-1,A)
        quickSort(pIndex+1,end,A)
    return A

A = [4,1,8,2,5,3,13,200,33]
ans = quickSort(0,len(A)-1,A)
print(ans)
        