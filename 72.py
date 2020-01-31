def gen(n):
    for i in range(0,n+1):
        if i%5==0 and i%7==0:
            yield i
x=[]

for i in gen(100):
    x.append(i)
print(*x,sep=',')
