""" 
recursive_tree.py draws a recursive tree.
assignment: lecture
language: python3
author: RIT CS Dept.
"""

import turtle

WIN_DIM = 600 # Window height and width, in pixels
BORDER_WIDTH = 2 # margin on edges of window

# function definitions

def draw_tree( segments, size ):
    """
    draw_tree recursively draws the tree.

    segments -- NonNegInteger;
        number of line segments from the base of the tree to
        the end of any branch should be integral and non-negative.
    size -- PosNumber;
        length of tree "trunk" to draw should be (strictly) positive.

    pre-conditions:
        segments >= 0, size > 0.
        turtle is at base of tree,
        turtle is facing along trunk of tree,
        turtle is pen-down.
    post-conditions:
        a segments-level tree was drawn on the canvas,
        turtle is at base of tree,
        turtle is facing along trunk of tree,
        turtle is pen-down.
    """
    if segments == 0:
        # base case: draw nothing
        pass
    elif segments > 0:
        # recursive case: draw trunk and two sub-trees
        turtle.forward( size )
        turtle.left( 45 )
        draw_tree( segments - 1, size / 2 )
        turtle.right( 90 )
        draw_tree( segments - 1, size / 2 )
        turtle.left( 45 )
        turtle.forward( -size )


# SETUP CODE

def init_world( window_size, boundary_width ):
    """
    init_world initializes the drawing by establishing its pre-conditions.

    window_size -- the length and height of the drawing area
    boundary_width -- the thickness of the window boundary

    pre-conditions: 
    post-conditions:
        coordinate system is as specified by the parameter values
        turtle is at origin,
        turtle is facing North,
        turtle is pen-down.
    """
    
    turtle.setup( WIN_DIM, WIN_DIM )

    turtle.setworldcoordinates( -window_size - boundary_width,
                                -window_size - boundary_width,
                                window_size + boundary_width,
                                window_size + boundary_width )
    turtle.clear()
    turtle.home()  # turtle is at origin, facing east, pen-down
    turtle.left( 90 )  # turtle is facing North
    turtle.down()  # turtle is pen-down
    turtle.pensize( 2 )
    #turtle.speed( 0 )   # makes it fast


def init_world_and_draw_tree( segments, size ):
    """
    init_world_and_draw_tree prints a message, initializes the world,
    draws an instance of the recursive tree, and waits for ENTER.

    segments -- NonNegInteger;
        number of line segments from the base of the tree to
        the end of any branch should be integral and non-negative.
    size -- PosNumber;
        length of tree "trunk" to draw should be (strictly) positive.
    """
    print( "Drawing recursive tree with", (segments, size) )
    init_world( size * 2, BORDER_WIDTH )
    # The above "2" is a "fudge factor" to try to
    # keep the drawing from extending beyond the window.
    draw_tree( segments, size )

def prompt_and_draw_tree():
    """
    prompt_and_draw_tree prompts for number of line segments from the
    base of the tree to the end of any branch and length of tree "trunk"
    and draws an instance of the recursive tree.
    """
    segments = int( input( "Enter 'segments' (a non-negative integer): " ) )
    size = int( input( "Enter 'size' (a positive integer): " ) )
    init_world_and_draw_tree( segments, size )

# script execution/run
if __name__ == "__main__":
    prompt_and_draw_tree()
    print( "Close the window to quit." )
    turtle.done()