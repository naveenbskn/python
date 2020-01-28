"""
14. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""
a=int(input())
aa=a*11
aaa=a*111
aaaa=a*1111
print(a+aa+aaa+aaaa)
