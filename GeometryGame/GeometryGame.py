class Point(object):
    """
    Class defining a 2D point within a euclidian space.

    Parameters
    ----------
    x :: float - x coordinate
    y :: float - y coordinate

    Methods
    ----------

    falls_in_rectangle :: takes a Rectangle object instance and etermines if the point instance 
        falls within the rectangle instance, returns bool

    
    distance :: takes a Point object instance and calculates the distance from the given instance point to 
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
        rectangle :: Rectangle object - contains the Point objects defining the loer left vertex and upper right
        vertex of the rectangle, see Rectangle

        Returns
        -----------
        boolean :: True if point is within the defined rectangle, false otherwise

        """
        if (rectangle.lowerLeft.x <= self.x <= rectangle.upperRight.x) \
            & (rectangle.lowerLeft[1] <= self.x <= rectangle.upperRight[1]):
            return True
        else:
            return False
    
    def distance(self, newPoint):
        """
        Calculate and return the euclidian distance from the instance point (self.x, self.y) to the new point
        (newX, newY)

        Parameters
        -----------
        newPoint :: Point object - new point objec coordinates (newPoint.x, newPoint.y) to calculate distance relative to

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
    lowerLeft :: Point object - lower left vertex coordinates of the rectangle (x, y)

    upperRight :: Point object - upper right vertex coordinates of the rectangle (x, y) - see Point

    Methods
    -----------


    """

    def __init__(self, lowerLeft, upperRight):
        self.lowerLeft = lowerLeft
        self.upperRight = upperRight
