import re, string
a=input() 
if len(a) <= 300:
    
    w=[]
    a=a.split()



    res = {i : a.count(i) for i in set(a)}
   

    for i in sorted (res.keys()) :  

        w.append(i)
    w.pop(0)
    
    
    for i in w :
        t=list(res.values())[list(res.keys()).index(i)] 
        
        print("{}:{}".format(i,t))
