def a(n):
    if(n%2==0):
       return True
    else:
        return False


x=[int(i)for i in input().split(',')]
q=filter(a,x)

print(list(q))
