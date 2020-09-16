#pyhton class that calculates area of rectangle


class Rec():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rec(5, 6)
print(newRectangle.rectangle_area())