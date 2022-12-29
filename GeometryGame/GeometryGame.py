class Point(object):
    """
    Class defining a 2D point within a euclidian space.

    Parameters
    ----------
    x : float - x coordinate
    y : float - y coordinate

    Methods
    ----------

    falls_in_rectangle: takes a Rectangle object instance and etermines if the point instance 
        falls within the rectangle instance, returns bool

    
    distance: takes a Point object instance and calculates the distance from the given instance point to 
        the argument point instance, returns float
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        """
        Given the lower left rectangle vertex coordinates and and the upper right rectangle vertex coordinates, 
        return if the insance point (self.x, self.y) is within the rectangle defined by the lower left and upper 
        right vertices.

        Parameters
        -----------
        rectangle: Rectangle object - contains the Point objects defining the loer left vertex and upper right
        vertex of the rectangle, see Rectangle

        Returns
        -----------
        boolean: True if point is within the defined rectangle, false otherwise

        """
        if (rectangle.firstPoint.x <= self.x <= rectangle.secondPoint.x) \
            & (rectangle.firstPoint.y <= self.y <= rectangle.secondPoint.y):
            return True
        else:
            return False
    
    def distance(self, newPoint):
        """
        Calculate and return the euclidian distance from the instance point (self.x, self.y) to the new point
        (newX, newY)

        Parameters
        -----------
        newPoint: Point object - new point objec coordinates (newPoint.x, newPoint.y) to calculate distance relative to

        Returns
        -----------
        float - distance between instance point and new point

        """
        return ((newPoint.x - self.x)**2 + (newPoint.y - self.y)**2)**0.5

class Rectangle(object):
    """
    Class defining a rectangle in a 2D euclidian space. Rectangle object will be used to define whether or not a user
    defined point object is within the area defined by the rectangle object.

    Parameters
    -----------
    firstPoint: Point object - lower left vertex coordinates of the rectangle (x, y)

    secondPoint: Point object - upper right vertex coordinates of the rectangle (x, y) - see Point

    Methods
    -----------
    area: calculates the area of the Rectangle instance and returns a float

    """

    def __init__(self, firstPoint, secondPoint):
        self.firstPoint = firstPoint
        self.secondPoint = secondPoint

    def area(self,):
        """
        Calculates the area of the Rectangle instance based upon firstPoint and secondPoint
    
        Parameters
        -----------
        None

        Returns
        -----------
        area: float - unitless area of 2D Rectangle object
        """

        return (abs(self.secondPoint.x - self.firstPoint.x) * abs(self.secondPoint.y - self.firstPoint.y))

# Implementation of Command Line Game
import random

# Generate Random Rectangle by generating random two points
randPoint1 = Point(random.uniform(0,9), random.uniform(0,9))
randPoint2 = Point(random.uniform(9,19), random.uniform(9,19))
rectangle = Rectangle(randPoint1, randPoint2)

#Print out the Rectangle Coordinates
print("\n*** WELCOME TO THE RECTANGLE GUESSING GAME ***\n")
print("Rectangle vertices coordinates: {}, {} and {}, {}\n".format(rectangle.firstPoint.x, rectangle.firstPoint.y, 
    rectangle.secondPoint.x, rectangle.secondPoint.y))

#Ask for User Input to Guess Point Within Rectangle
print("Guess point coordinates within the rectangle")
userPoint = Point(float(input("Guess X: ")), float(input("Guess Y: ")))

#Ask User to Guess Area of Rectangle
userArea = float(input("Guess the rectangle area: "))

#Report User Results
print("Was your point guess within the rectangle?", userPoint.falls_in_rectangle(rectangle=rectangle))
print("Your rectangle area guess was off by:", rectangle.area() - userArea)