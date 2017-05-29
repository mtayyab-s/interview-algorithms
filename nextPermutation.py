'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
'''
nums= [3,2,1]
n = len(nums)

def reverse(a,i,j):
    while(i<j):
        a[i],a[j]=a[j],a[i]
        i=i+1
        j=j-1
    return a
index1 = -1
index2=-1

# find the max index such that nums[i]<nums[i+1]
for i in range(n-1):
    if nums[i]<nums[i+1]:
        index1 = i
# if no such index is found return sorted nums

# else find the max index greater that index1 where nums[index]<nums[i]
if index1!=-1:
    for i in range(index1+1,n):
        if nums[index1]<nums[i]:
            index2=i

    nums[index1],nums[index2] = nums[index2],nums[index1]
    nums = reverse(nums,index1+1,n-1)
else:
    nums.sort()
print(nums)