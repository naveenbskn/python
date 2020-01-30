b=[]
w=0
d=0
c=[]
s=0
while(1):
    a=input()
    if a:
        b.append(a)
    else:
        break
print(b)
for i in range(len(b)):
    if(b[i][0]=='D'):
        s=s+int(b[i][2:])
        
    elif(b[i][0]=='W'):
        s=s-int(b[i][2:])
    
print(s)
    
        
