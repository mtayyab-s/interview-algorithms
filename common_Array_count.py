'''
Given two unsorted arrays arr1[] and arr2[]. They may contain duplicates.
For each element in arr1[] count elements less than or equal to it in array arr2[].
http://www.geeksforgeeks.org/element-1st-array-count-elements-less-equal-2nd-array/
'''


def bSearch(num, arr2):
    start = 0
    end = len(arr2) - 1

    ans=-1
    while (start <=end):
        mid = int((start + end) / 2)
        if arr2[mid]<=num:
            start = mid +1
        else:
            end = mid -1
    return end

arr1 = [1, 2, 3, 4, 7, 9]
arr2 = [0, 1, 2, 1, 1, 4]
arr2 = sorted(arr2)

for j in arr1:

    ind =bSearch(j,arr2)+1
    print(ind)










