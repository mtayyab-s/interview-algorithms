 '''
 The challenge is to find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.
 '''

def twoSum(S,target):
    hashtable={}
    result = []
    for i in S:
        if (target-i) in hashtable:
            temp = [i,abs(target-i)]
            result.append([temp])
        hashtable[i] = i
    print(result)
        
            
           
    
A =[3, 5, 2, -4, 8, 11] 

twoSum(A,7)
    