'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
'''

def removeDuplicates(nums):
    j=1
    n=len(nums)
    for i in range(1,n):
        if nums[i]!=nums[i-1]:
            nums[j] = nums[i]
            j=j+1
    nums =nums[0:j]
    return(len(nums))  
nums = [1,1,1,2,2,2,4,4,4,5,5]
solution = removeDuplicates(nums)
print(solution)