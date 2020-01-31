def gen(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
x=[]
for i in gen(10):
    x.append(i)
print(*x,sep=',')


