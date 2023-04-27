class Rectangle(object):
    """
    Definition of rectangle object for drawing a colored rectangle.

    Parameters
    -----------
    x : int
        x horizontal dimension location of the top left vertex of the retangle
    y : int
        y verticle dimension location of the top left vertex of the retangle
    width : int
        Pixel width along horizontal dimension of rectangle
    height : int
        Pixel height along verticle dimension of rectangle
    color : array
        1-dimensional array of RGB color of image [R(0-255), B(0-255), G(0-255)]
    
    Methods
    -----------
    draw(canvas) : 
        Creates Canvas object for saving the rectangle image as an image file
    """

    def __init__(self, x:int, y:int, width:int, height:int, color:tuple):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self, canvas):
        # Draw desired shape into existing canvas
        canvas.data[self.y: self.y + self.height, self.x: self.x + self.width] = self.color

class Square(Rectangle):
    """
    Child class of Rectangle, where the width and height are equal. Creates object for drawing a colored square.

    Parameters
    ----------
    x : int
        x horizontal dimension location of the top left vertex of the square
    y : int
        y verticle dimension location of the top left vertex of the square
    side : int
        Pixel length along horizontal and veritcal dimension of square
    color : array
        1-dimensional array of RGB color of image [R(0-255), B(0-255), G(0-255)]
    
    Methods
    ----------
    draw(canvas) : 
        Creates Canvas object for saving the rsquare image as an image file
    """

    def __init__(self, x:int, y:int, side:int, color:tuple):
        super().__init__(x=x, y=y, width=side, height=side, color=color)
    
    def draw(self, canvas):
        super().draw(canvas)