def a(n):
    if(n%2==0):
       return True
    else:
        return False
def b(m):
    return m*m

x=[int(i)for i in input().split(',')]
q=filter(a,x)
ww=map(b,q)
print(list(ww))
