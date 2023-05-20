class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea(self):
        return self.a * self.b

rect_1 = Rectangle(10, 20)

print(rect_1.getArea())
