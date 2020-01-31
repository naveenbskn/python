def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100
n= int(input())
a = 0
if n==0:
    print(1)
else:
    print(f(n))
 


