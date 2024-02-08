import math

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_x, other_y):
        return math.sqrt((self.x - other_x)**2 + (self.y - other_y)**2)

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
point1 = Point(x1, y1)

x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
point2 = Point(x2, y2)

point1.show()
point2.show()

distance = point1.dist(point2.x, point2.y)
print("Distance between the points:", distance)