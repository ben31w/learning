# More Pygame info: 
#  http://cs.roanoke.edu/Fall2013/CPSC120A/pygame-1.9.1-docs-html/
terms = {
    'Pygame': "a colllection of Python modules that contains helpful tools to "
        "manage the graphics, animations, and sounds of a video game project.",
    'pip': "a standard Python module that acts as a package management system, "
        "allowing users to download and install Python packages. Most versions "
        "of Python come with pip preinstalled.",
    # To use pip to install pygame, enter this line into a terminal window:
    #  python -m pip install --user pygame
    'surface': "a part of the screen where a game element can be displayed.",
    'event': "an action that the user performs while playing the game, such as "
        "pressing a key or moving the mouse.",
    'event loop': "a loop that listens for events and performs appropriate "
        "tasks depending on the types of events that occur. In Pygame, an "
        "example of an event loop would be: for event in pygame.event.get():",
    'rect': "a rectangle that has attributes for the x- and y-coordinates of "
        "its center and its top, bottom, left, and right edges. The default x "
        "and y attributes of a rect are the x- and y- coordinates of its top "
        "left corner. Pygame allows you to treat all game elements like rects, "
        "which is efficient for detecting simple collisions.",
    # In Pygame, you usually use surfaces to represent the appearace of objects,
    #  and rectangles to represent their position.
    'helper method': "a method that is reused often inside other methods or "
        "parts of a program. Helper methods can be written inside a class, but "
        "they aren't meant to be called through an instance. In Python, a "
        "single leading underscore indicates a helper method.",
}

functions = {
    'pygame.init()': "initializes all imported Pygame modules., It is often "
        "the first line written when defining the __init__() method in a class "
        "that uses Pygame modules.",
    'pygame.display.set_mode()': "creates a display window surface. When given "
        "a tuple with two ints, the ints act as the width and height of the "
        "display window (in pixels).",
    'pygame.event.get()': "returns a list of events that have taken place "
        "since the last time the function was called.",
    'pygame.display.flip()': "makes the most recently drawn screen visible.",
    'Surface.get_rect()': "returns a Surface's rect attribute.",
    'pygame.image.load()': "loads a given image and returns it as a surface.",
    'Surface.blit()': "when given an image and its rect, draws the image to a "
        "surface at the position specified by the rect.",
    'pygame.font.SysFont()': "loads and returns a Font object when given a "
        "font name and a font size. If the font name is not found in the "
        "system's fonts, the system's default font will be used. This function "
        "also accepts Boolean parameters for bold and italic.",
    'Font.render()': "creates and returns a Surface with specified text on it. "
        "This method requires 3 parameters: a message to be displayed, a "
        "Boolean value to turn antialiasing (text-smoothing) on or off, and a "
        "text foreground color. It also accepts a fourth parameter for the "
        "text's background color.",
    'pygame.mouse.get_pos()': "returns a tuple containing the mouse cursor's "
        "x- and y-coordinates.",
}

classes = {
    'pygame.Rect': "creates a rect when given 4 parameters: the x-coordinate "
        "of the top left corner, the y-coordinate, the width, and the height.",
    'pygame.sprite.Sprite': "a simple base class for visible game objects. "
        "Sprites enable you to group related game elements and act on all the "
        "grouped elements at once.",
    'pygame.sprite.Group': "a container class for many sprites. Calling a "
        "function on a Group will call the function for each Sprite in the "
        "Group.",
    'pygame.font.Font': "a class for storing fonts.",
}

print("-------------------terms-------------------\n")
for term, definition in sorted(terms.items()):
    print(f"{term}: {definition}\n")

print("-------------------functions-------------------\n")
for function, description in sorted(functions.items()):
    print(f"{function}: {description}\n")

print("-------------------classes-------------------\n")
for class_name, description in sorted(classes.items()):
    print(f"{class_name}: {description}\n") 