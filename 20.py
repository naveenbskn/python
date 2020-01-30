class mine:
    def my_gen(x,y):
        for i in range(x,y+1):
            if i%7==0:
                yield i
for item in mine.my_gen(0,100):
    print(item)
