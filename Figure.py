class Trapezoid:
    def __init__(self, x, y, width,):
        self.x = x
        self.y = y
        self.width = width


    def __str__(self):
        return f'Trapezoid : {self.x}, {self.y}, {self.width}.'

rect_1 = Trapezoid(5, 10, 50)
print(rect_1)