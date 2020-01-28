"""
9. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""
b=[]
while(1):
    a=input()
    if a:
        b.append(a)
    else:
        break;
for i in b:
   print (i.upper())
