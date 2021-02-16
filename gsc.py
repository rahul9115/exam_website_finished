from itertools import permutations
a=int(input())
l=[]
l1=[]
for i in range(1,a+1,1):
    l.append(i)
perm=permutations(l)    

for i in list(perm):
    k=0
    
    for j in range(0,len(i),1):
        if i[j]==(j+1):
            
            continue
        else:
            k=k+1
    if k==a:
        l1.append(i)


print(len(l1))            