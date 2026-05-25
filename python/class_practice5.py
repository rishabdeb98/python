class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.area=width*height
r1=Rectangle(5,3)
print(r1.area)