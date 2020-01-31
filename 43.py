def a(n):
    return n**2

x=[int(i)for i in input().split(',')]
q=map(a,x)
print(list(q))
