i=int(input())
a=0
b=1
c=a+b
print(a)
print(b)
print(c)
j=0
while(j<i-2):
    
    (a,b)=(b,a)
    (b,c)=(c,b)
    c=a+b
    print(c)

    j=j+1
    
