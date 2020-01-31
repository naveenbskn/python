a=[]
b=input()
b=b.split()
try:
    for i in b:
        if i.isdigit():
            
            a.append(i)
except:
    w=1
print(a)
