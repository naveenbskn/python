a=input()
a=a.split(',')
for i in a:
    if(len(i)>=6 and len(i)<12):
        lower=0
        upper=0
        sym=0
        num=0
        for j in range(len(i)):

            if(i[j].isalpha()):
                if(i[j].islower()):
                    lower=1
                if(i[j].isupper()):
                    upper=1

            if(i[j].isalpha()==False):
                if(i[j].isdigit()):
                    num=1
                else:
                    sym=1
        if(lower==1 and upper==1 and sym==1 and num==1):
            print(i)
             
            
            

    
