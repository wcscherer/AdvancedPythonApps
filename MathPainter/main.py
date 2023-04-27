"""
Command Line Interface script that generates a black or white colored canvas (of user defined dimension) overtop of 
which the user can define the dimensions and colors of square and rectangle shapes to decorate the canvas. The
resulting drawing is saved locally as a png. The script asks for inputs until the user supplies 'stop' or 'quit'
and upon quitting the image is saved locally. 
"""

from canvas import Canvas
from rectangle import Rectangle, Square

# constansts and defined RGB colors
COLORS = {'white':(255, 255, 255), 'black':(0,0,0)}

def collect_colors():
    """
    Asks user for intensity of red, blue, and green on a scale of 0 to 255 for RGB array.

    Parameters
    -----------
    NONE

    Returns
    -----------
    color : array[int]
        3-element array of RGB colors [R(int), B(int), G(int)]
    """
    while True:

        red   = abs(int(input("How much red should the shape have (0-255): ")))
        blue  = abs(int(input("How much blue should the shape have (0-255): ")))
        green = abs(int(input("How much green should the shape have (0-255): ")))

        # verify all colors within range
        if (red <= 255) and (blue <= 255) and (green <= 255):
            break
        else:
            print("ERROR - All colors intensities (i) must fall within 0 <= i <= 255")
            print(f"Current intensities: Red {red}, Blue {blue}, Green {green}")
            print("Retry selecting colors intensities...")
            continue

    return [red, blue, green]


if __name__ == "__main__":

    # Starting Banner
    print("\n**** Welcome to the Math Painter Command Line App ****\n")
    print("It's up to you to define the size and color of you canvas.")
    print("It's up to your imagination to determine what you choose to paint.\n")

    # Ask User for canvas color and dimensions
    print("Provide the background canvas dimensions and color.")
    canvasWidth = abs(int(input("Enter the canvas horizontal width in pixels to draw on: ")))
    canvasHeight = abs(int(input("Enter the canvas vertical height in pixels to draw on: ")))
    canvasColor = str(input("Enter the canvas color (black or white): ")).lower()

    # Generate Canvas instance
    try:
        canvas = Canvas(width=canvasWidth, height=canvasHeight, color=COLORS[canvasColor])
    except:
        raise ValueError(f"Canvas unable to be created with width {canvasWidth}, height {canvasHeight}, and color {canvasColor}")

    # Loop for generating the colored shapes on top of the canvas
    print("\nNow select the shapes and colors to decorate your canvas.\n")
    print("REMEMBER, type 'quit' or 'stop' to exit the app and save your painting.\n")
    while True:

        shape = input("What shape would you like to draw (rectangle or square). Type quit to exit: ")
        
        # create rectangle shape if selected
        if shape.lower() == 'rectangle':
            print("\nDefining Rectangle Shape")
            xR = int(input("Enter the x horizontal pixel location of the top left vertex within the canvas: "))
            yR = int(input("Enter the y vertical pixel location of the top left vertex within the canvas: "))
            widthR = int(input("Enter the pixel horizontal width: "))
            heightR = int(input("Enter the pixel vertical height: "))
            colorR = collect_colors()
            rectangle = Rectangle(x = xR, y=yR, width=widthR, height=heightR, color=colorR)
            # add rectangle to canvas
            try:
                rectangle.draw(canvas=canvas)
            except:
                RuntimeError(f"Rectangle at ({xR},{yR}) with dimensions ({widthR}, {heightR}) and color ({colorR}) could not be added to the canvas")
        
        # create square shape if selected
        elif shape.lower() == 'square':
            print("\nDefining Square Shape")
            xS = int(input("Enter the x horizontal pixel location of the top left vertex within the canvas: "))
            yS = int(input("Enter the y vertical pixel location of the top left vertex within the canvas: "))
            sideS = int(input("Enter the pixel side length: "))
            colorS = collect_colors()
            square = Square(x=xS, y=yS, side=sideS, color=colorS)
            # add square to canvas
            try:
                square.draw(canvas=canvas)
            except:
                RuntimeError(f"Square at ({xS},{yS}) with sides ({sideS}) and color ({colorS}) could not be added to the canvas")

        # if stop is requested, attempt to save figure and exit app
        elif shape.lower() == 'stop' or shape.lower() == 'quit' or shape.lower() == 'exit':
            print("EXITING...\n")
            print("Stopping drawing and saving painting.")
            fileName = input("Enter figure name path to save as PNG: ")
            try:
                canvas.make(imagePath=fileName)
                print(f"File successfully saved as {fileName}.png")
                print("\n**** You are exiting the Math Painter App ****\n")
            except:
                raise RuntimeError(f"Could not save canvas to {fileName}")
            break
        
        # catch if the user supplies another input that isn't covered.
        else:
            print(f"Shape type '{shape.lower()}' not supported. Please select a rectangle or square to draw. Type stop or quit to save your figure and exit.\n")
            continue

