from Rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.getArea())
print(rect_2.getArea())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),square_2.get_area_square())

figures = [rect_1,rect_2,square_1,square_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    else:
        print(figure.getArea())


circle_1 = Circle(2)

print(circle_1.get_area_circle())