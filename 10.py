"""
10. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""

a=input()
a=a.split()
a.sort()
try:
    
    for i in range (0,len(a)-1):
        if(a[i]== a[i+1]):
            a.pop(i)
except:
    w=1
print(*a)
    
