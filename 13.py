"""
13. Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""

a=input()
l=0
d=0
for i in range(0,len(a)):
    if a[i]>'a' and a[i]<'z':
        l=l+1
    try:
       int(a[i])
       d=d+1
    except:
        w=1
print("LETTERS "+str(l))
print("DIGITS "+str(d))
