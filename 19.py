a=[]
e=[]
while(1):
    b=input()
    if b:
        q=b.split(',')
        a.append(q)
    else:
        break
print(a)
for i in range(len(a)):
    tt=len(a[i][0])
    #e.sort(a[i][0][:tt])
    
a.sort()
print(a)   
        
