'''
* Knapsack Problem
* 11/27/2017
* Muhammad Tayyab
'''


wt = [1,3,4,5]

val = [1,4,5,7]

W = 7 

#initializing the array
ans = [[0]*(W+1) for i in range(len(wt))]


for i in range(len(wt)):
  for j in range(1,W+1):
    ans[i][j] = 1
  break

for i in range(1,len(wt)):
  for j in range(0,W+1):
    if j<wt[i]:
      ans[i][j] = ans[i-1][j]
      
    else:
      temp= max(val[i] + ans[i-1][j-wt[i]],ans[i-1][j])
      ans[i][j] = temp
     
     
print(ans)