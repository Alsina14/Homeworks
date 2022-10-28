class Point(object):
    """represents a point on a two-dimensional plane"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        


class Triangle(Point):
    """Represents a triangle. The constructor accepts 3 triangle vertices - objects of the Point class"""
    def __init__(self, a, b, c ):
        self.point_1 = a
        self.point_2 = b
        self.point_3 = c
        self.area = self.get_area()
        self.perimeter = ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5 + ((c.x - b.x)**2 + (c.y - b.y)**2)**0.5 + ((a.x - c.x)**2 + (a.y - c.y)**2)**0.5 
        
    def is_inside(self, p):
        """accepts a point and returns True if the point lies inside the triangle and False otherwise"""
        s1 = Triangle(a, b, p).area
        s2 = Triangle(a, p, c).area
        s3 = Triangle(p, b, c).area
        return self.area == s1 + s2 + s3
    
    def get_area(self):
        return 0.5 * abs(self.point_1.x * (self.point_2.y - self.point_3.y) +
                         self.point_2.x * (self.point_3.y - self.point_1.y) + 
                         self.point_3.x * (self.point_1.y - self.point_2.y))

class ColouredTriangle(Triangle):
    def __init__(self, colour, *args):
        super().__init__(*args)
        self.colour = colour

    
a = Point(0, 0)
b = Point(0, 1)
c = Point(1, 0)
k = Triangle(a, b, c)
print("Area =", k.area)
print("Perimeter =", k.perimeter)
    
p = Point(0.5, 0.1)
print("Is point inside?", k.is_inside(p))

e = Point(1, 0)
g = Point(1, 1)
f = Point(3, 0)
t = ColouredTriangle('red',e, g, f)
print("Area_1 =", t.area)
print("Perimeter_1 =", t.perimeter)
    
p1 = Point(1.5, 0.1)
print("Is point inside?", t.is_inside(p1))


    