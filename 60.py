a=input()
c=0
for i in a:
    if i=='@':
        break
    else:
        c=c+1
print(a[:c])
