a=input()
a=a.split(',')
b=[]
a=[int(i) for i in a]
for i in a:
    if i%2==0:
        pass
    else:
        b.append(i*i)
print(*b,sep=",")
