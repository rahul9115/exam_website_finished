

class op_overload:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a,self.b)
        
        
    def __add__(self,o):
        
        real=self.a+o.a
        img=self.b+o.b
        
        print(real,img)
        
        
        
                
if __name__=="__main__":
    
    o1=op_overload(2,3)
    o2=op_overload(4,5)
    o3=o1+o2
    
    
    
    
 
 



