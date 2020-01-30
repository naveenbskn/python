a=input()
b=input()
c=[]
d=[]
e=[]
for i in a:
    c.append(i)
for i in b:
    d.append(i)
for i in range(len(c)):
    for j in range(len(d)):
        if c[i]==d[j]:
            e.append(c[i])
print(e)

