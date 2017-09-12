'''
MergeSort time complxity is nlog(n) worst case
'''

def mergeSort(A):
    n = len(A)
    if n<2:
        return A
    mid =int(n/2)
    left = []
    right = []
    for i in range(mid):
        left.append(A[i])
    for i in range(mid,n):
        right.append(A[i])
    #print(left)
    #print(right)
    mergeSort(left)
    mergeSort(right)
    merge(left,right,A)
    return A

def merge(left,right,A):
    nLeft = len(left)
    nRight= len(right)
    i=0
    j=0
    k=0
    while(i<nLeft and j<nRight):
        if left[i]< right[j] :
            A[k] = left[i]
            i=i+1
        else:
            A[k] = right[j]
            j=j+1
        k=k+1
    while(i<nLeft):
        A[k] = left[i]
        i=i+1
        k=k+1
    while(j<nRight):
        A[k]=right[j]
        j=j+1
        k=k+1
    return A
    
A = [3,5,7,8,3,1,90,15]
ans = mergeSort(A)
print(ans)
        