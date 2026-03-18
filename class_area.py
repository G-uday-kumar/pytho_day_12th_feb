class Shape:
    def area(self):
        print("area of shape")
class Circle(Shape):
    def area(self):
        radius=6
        print("area of circle", 3.14*radius**2)
c=Circle()
c.area()
s=Shape()
s.area()