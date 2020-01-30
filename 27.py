def add(c):
    s=0
    for i in c:
        s=s+i
    print(s)
a=input()
a=a.split()
a=[int(i) for i in a]
add(a)
