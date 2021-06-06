class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
       print("A Polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter        

class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")

class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")
        Polygon.display_info(self)

t1 = Triangle([25,27,28])
permeter = t1.get_perimeter()
print("perimeter of traingle is", permeter)

t1.display_info()

q1 = Quadrilateral([1, 2, 3, 4])
peremeter = q1.get_perimeter()
print("perimeter of quadrilateral is",peremeter)
q1.display_info()
