class Point:
    """
    Class defining a 2D point within a euclidian space.

    Parameters
    ----------
    x :: float - x coordinate
    y :: float - y coordinate

    Methods
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowerLeft, upperRight):
        """
        Given the lower left rectangle vertex coordinates and and the upper right rectangle vertex coordinates, 
        return if the insance point (self.x, self.y) is within the rectangle defined by the lower left and upper 
        right vertices.

        Parameters
        -----------
        lowerLeft :: tuple of floats - lower left rectangle vertex coordinates (x,y)

        upperRight :: tuple of floats - upper right rectangle vertex coordinates (x,y)

        Returns
        -----------

        boolean :: True if point is within the defined rectangle, false otherwise

        """
        if (lowerLeft[0] <= self.x <= upperRight[0]) \
            & (lowerLeft[1] <= self.x <= upperRight[1]):
            return True
        else:
            return False
    
    def distance(self, newX, newY):
        """
        Calculate and return the euclidian distance from the instance point (self.x, self.y) to the new point
        (newX, newY)

        Parameters
        -----------
        newX :: float - x coordinate of new point
        
        newY :: float - y coordinate of new point

        Returns
        -----------
        float - distance between instance point and new point

        """
        return ((newX - self.x)**2 + (newY - self.y)**2)**0.5
