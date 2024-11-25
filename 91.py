class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def para(self):
        return 2*(self.length + self.width)
    
R1 = Rectangle(12,2)
print(f"Area : {R1.area()}")
print(f"Parameter : {R1.para()}")