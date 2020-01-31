class shape:
    def area(self):
        return 0
class square(shape):
    def __init__(self,l):
        self.l=l
    def area(self,l):
        print(super().area())
        print(self.l*self.l)
s=square(4)
s.area(s.l)
