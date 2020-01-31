a=tuple(int(x) for x in input().split(','))
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print(tuple(b))



