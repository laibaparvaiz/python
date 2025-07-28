import math
class Point:
    def __init__(self,x=0.0, y=0.0):
        self.__x = x
        self.__y = y
        
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y
    
    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)
    
    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())
    
class Triangle:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        side1 = self.a.distance_from_point(self.b)
        side2 = self.b.distance_from_point(self.c) 
        side3 = self.c.distance_from_point(self.a) 
        return side1 + side2 + side3
    
    def __str__(self):
        return f"Triangle with points: ({self.a.getx()}, {self.a.gety()}), " \
               f"({self.b.getx()}, {self.b.gety()}), " \
               f"({self.c.getx()}, {self.c.gety()})"

a = Point(0, 0)
b = Point(3, 0)
c = Point(0, 4)

triangle = Triangle(a, b, c)
print(triangle)
print("Perimeter:", triangle.perimeter())