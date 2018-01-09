'''
http://practice.geeksforgeeks.org/problems/maximum-tip-calculator/0
Maximum Tip Calculator
'''

t = int(input())
for i in range(t):
    n,count_a,count_b = input().split()
    count_a =int(count_a)
    count_b = int(count_b)
    a = [int(k) for k in input().split()]
    b = [int(j) for j in input().split()]
    diff=[]
    for j in range(int(n)):
        diff.append(abs(a[j] - b[j]))
    ind = sorted(range(len(diff)), key=lambda k: diff[k],reverse = True)
    sum =0
    
    for p in ind:
        if(a[p]>b[p] and count_a>0):
            sum = sum+a[p]
            count_a =count_a -1
        elif (a[p]<b[p] and count_b>0):
            sum = sum+b[p]
            count_b =count_b -1
        elif (a[p]>b[p] and count_a<=0):
            sum = sum+b[p]
            count_b =count_b -1
        elif (a[p]<b[p] and count_b<=0):
            sum = sum+a[p]
            count_a =count_a -1
        else:
            if count_a>=count_b:
                sum =sum+a[p]
                count_a =count_a-1
            else: 
                sum =sum+b[p]
                count_b =count_b-1
            
    
    print(sum)