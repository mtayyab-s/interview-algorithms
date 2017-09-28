#Longest Common subsequence (dynamic programming)

s1 ="adefnl"
s2 = "beflp"
w, h = len(s1)+1, len(s2)+1
Matrix = [[0 for x in range(w)] for y in range(h)]

for i in range(0,len(s2)):
    for j in range(0,len(s1)):
        if(s1[j]== s2[i]):
            Matrix[i+1][j+1]=Matrix[i-1+1][j-1+1]+1
        else:
            Matrix[i+1][j+1] = max(Matrix[i-1+1][j+1],Matrix[i+1][j-1+1])

#print Matrix[len(s2)][len(s1)]
ans = []
i=5
j=6
while(i>0 and j>0):
    if Matrix[i][j]==Matrix[i-1][j]:
        i=i-1
    elif Matrix[i][j] == Matrix[i][j-1]:
        j=j-1
    else:
        ans.append(s1[j-1])
        i=i-1
        j=j-1

print ans
