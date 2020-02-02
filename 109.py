a=int(input())
b=input().split()
c=[]
b.sort()
for i in range(len(b)-1):
    if(b[i]==b[i+1]):
        b.pop(i)
print(b[-2])
