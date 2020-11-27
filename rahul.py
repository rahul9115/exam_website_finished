def calcTotal(input1,input2):
    tax=0
    diff=0
    for i in range(0,int(input1/2)+1,1):
        left=i
        right=input1-i-1
        if i<int(input1/2):

            diff_left=input2[left]-input2[0]
            diff_right=input2[right]-input2[0]
            print(diff_left,diff_right)
            if diff_left>=1000:
                tax=int(tax+((diff_left)/10))
            if diff_right>=1000:
                tax=int(tax+((diff_right)/10))  
        else:
            diff_left=input2[left]-input2[0]
            if diff_left>=1000:
                tax=int(tax+((diff_left)/10))


        
    return tax        
if __name__=="__main__":
    length=5
    array=[1000,2000,3000,4000,5000]
    print(calcTotal(length,array))
