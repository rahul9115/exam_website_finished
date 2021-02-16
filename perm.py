import copy
str1="ABC"
str2=list(str1)

m=0
l=0
for i in range(0,3,1):
    str4=copy.deepcopy(str2)
    temp=str4[l]
    str4[l]=str4[i]
    str4[i]=temp
    
    str3=copy.deepcopy(str4)
    
    for j in range(1,3,1):
        l=1
        str3=copy.deepcopy(str4)
        temp=str3[j]
        str3[j]=str3[l]
        str3[l]=temp
        print(str3)
    l=0    
       
        
        
            
    


        
    
    
