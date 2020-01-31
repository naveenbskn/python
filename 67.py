n= int(input())
a = 0

for i in range(1,n+1):
    a = a+(i/(i+1))

print(round(a,2))
