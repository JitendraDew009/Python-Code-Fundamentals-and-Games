# Define a circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which claculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    
    def Area(self):
        return (22/7) * self.radius ** 2
       
        
    def Perimeter(self):
        return 2 * (22/7) * self.radius
        

c1 = Circle(21)
print("Area of Circle: ", c1.Area())
print("Perimeter of Circle : ", c1.Perimeter())
        