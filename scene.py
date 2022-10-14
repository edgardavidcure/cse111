# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing




def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_cloud(canvas, 80, 30, 300, 310)
    draw_cloud(canvas, 80, 40, 500, 380)
    draw_cloud(canvas, 80, 30, 50, 400)
    draw_ground(canvas, scene_width, scene_height)
    draw_sun(canvas, 700, 200, 500)
    draw_pine_tree(canvas, 200, 150, 400)
    draw_pine_tree(canvas, 100, 50, 320)
    draw_street(canvas, 900, 500, 800)

    


    
    
    
        


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    

    
    
    

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_cloud(canvas, diameter, space, x, y):
        
        interval = diameter - space

        for i in range(3):
            draw_oval(canvas, x, y, x + diameter, y + diameter, outline="white",
                    fill="white")
            x += interval


def draw_street(canvas, center_x, scene_height, scene_width):
    
    
    street_height = scene_height / 3
    street_width = scene_width / 9
    

    center_x = (center_x / 2)

    draw_line(canvas, center_x, 0 , center_x, street_height, width=street_width, fill="black")
    space_between_lines = 5
    interval = space_between_lines
    for i in range(2): 
    
        draw_line(canvas, center_x, 0, center_x, street_height, width=2, fill="yellow")

        center_x += interval

        



def draw_sun (canvas, x, y, diameter):
    draw_oval(canvas, x, y, x + diameter, y + diameter, outline="yellow", fill="yellow")


    
        
        

# Call the main function so that
# this program will start executing.
main()