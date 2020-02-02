a=int(input())
b=input().split()
c=int(input())
d=input().split()
e=[]
for i in range(0,len(b)):
    if(b[i]==d[i]):
        pass
    else:
        e.append(b[i])
        e.append(d[i])
e.sort()
for i in e:
    print(i)
