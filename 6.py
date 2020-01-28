"""
6. Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
import math
c=50
h=30
d=input()
q=[]
d=d.split(',')
r=[int(i) for i in d]
for i in r:
    t=(2*c*i)/h
    e=math.sqrt(t)
    q.append(round(e))
for i in q:
    print(i,end=" ")
