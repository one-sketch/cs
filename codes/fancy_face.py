""" 
fancy_face.py draws a fancy face.

assignment: lecture
language: python3
author: RIT CS Dept. mtf@cs.rit.edu, Matthew Fluet
"""

# imports

import turtle

# definitions

def init_world():
    """
    init_world initializes the drawing by establishing its pre-conditions.

    pre-conditions: N/A (not applicable)
    post-conditions:
                     coordinate system is (-600,-600) to (600,600)
                     turtle is at origin,
                     turtle is facing North,
                     turtle is pen-up.
    """
    turtle.setup( 600, 600 )
    reset_world()


def reset_world():
    turtle.clear()
    turtle.home()  # turtle is at origin, facing east, pen-down
    turtle.left( 90 )  # turtle is facing north
    turtle.up()  # turtle is pen-up
    turtle.pensize( 2 )
    turtle.speed( 0 )


def draw_border():
    """
    Draw a circle for the outline of the face.
    """
    turtle.right( 90 )
    turtle.down()
    turtle.circle( 100 )
    turtle.up()
    turtle.left( 90 )

def draw_mouth( mouth_type ):
    """
    Draw a mouth 60 points wide (30 units per side), 40 points above
    the bottom of the face.

    mouth_type -- String ('smile' or 'frown');
                 determines whether the mouth is a smile or a frown
    """
    turtle.forward( 40 )
    if mouth_type == "smile":
        turtle.left( 65 )
        turtle.forward( 30 )
        turtle.left( 180 )
        turtle.down()
        turtle.forward( 30 )
        turtle.left( 50 )
        turtle.forward( 30 )
        turtle.left( 180 )
        turtle.up()
        turtle.forward( 30 )
        turtle.left( 65 )
    elif mouth_type == "frown":
        turtle.left( 115 )
        turtle.forward( 30 )
        turtle.left( 180 )
        turtle.down()
        turtle.forward( 30 )
        turtle.right( 50 )
        turtle.forward( 30 )
        turtle.left( 180 )
        turtle.up()
        turtle.forward( 30 )
        turtle.left( 115 )
    else:
        turtle.left( 90 )
        turtle.forward( 30 )
        turtle.left( 180 )
        turtle.down()
        turtle.forward( 60 )
        turtle.left( 180 )
        turtle.up()
        turtle.forward( 30 )
        turtle.left( 90 )
    turtle.forward( 40 )
    turtle.left( 180 )

def draw_nose():
    """
    Draw a nose as an equilateral triangle with sides of 30, 70 points
    above the bottom of the face.
    """
    turtle.forward( 70 )
    turtle.left( 90 )
    turtle.down()
    turtle.forward( 15 )
    turtle.right( 120 )
    turtle.forward( 30 )
    turtle.right( 120 )
    turtle.forward( 30 )
    turtle.right( 120 )
    turtle.forward( 15 )
    turtle.up()
    turtle.left( 90 )
    turtle.forward( 70 )
    turtle.left( 180 )

def draw_eyes( eye_radius ):
    """
    Draw both eyes as circles, 100 points above the bottom of the
    face, and with centers 100 points apart.

    eye_radius -- PositiveInteger;
                 determines the radius of the eyes
    """
    turtle.forward( 100 )
    turtle.left( 90 )
    turtle.forward( 50 )
    turtle.right( 180 )
    draw_eye( eye_radius )
    turtle.forward( 100 )
    draw_eye( eye_radius )
    turtle.right( 180 )
    turtle.forward( 50 )
    turtle.left( 90 )
    turtle.forward( 100 )
    turtle.left( 180 )

def draw_eye( eye_radius ):
    """
    Draws a single eye as an 'eye_radius'-point-radius circle. 

    eye_radius -- PositiveInteger;
                 determines the radius of the eyes

    pre-conditions: turtle is facing East at the bottom of the eye location.
    post-conditions: turtle is in the same state as at the start.
    """
    turtle.down()
    turtle.circle( eye_radius )
    turtle.up()

def draw_fancy_face( mouth_type, eye_radius ):
    """
    Draw a fancy face.

    mouth_type -- String ('smile' or 'frown');
                 determines whether the mouth is a smile or a frown
    eye_radius -- PositiveInteger;
                 determines the radius of the eyes
    """
    draw_border()
    draw_mouth( mouth_type )
    draw_nose()
    draw_eyes( eye_radius )

def clear_and_draw_fancy_face( mouth_type, eye_radius, message="" ):
    """
    clear_and_draw_fancy_face prints a message, initializes the world,
    draws an instance of the fancy face, and waits for ENTER.

    mouth_type -- String ('smile' or 'frown');
                 determines whether the mouth is a smile or a frown
    eye_radius -- PositiveInteger;
                 determines the radius of the eyes
    message -- String; message to display
    """
    print( "Drawing face with", (mouth_type, eye_radius), ";", message )
    reset_world()
    draw_fancy_face( mouth_type, eye_radius )
    turtle.hideturtle()
    # the input function blocks until the user presses the enter/return key
    input( "Hit ENTER key to continue." )


def run_test_cases():
    """
    Run test cases using different arguments as input values.
    """

    init_world()

    # test case 1:
    clear_and_draw_fancy_face( "smile", 15, "(original face)" )

    # test case 2:
    clear_and_draw_fancy_face( "smile", 25, "(smile with big eyes)" )

    # test case 3:
    clear_and_draw_fancy_face( "frown", 5, "(frown with small eyes)" )

    # test case 4:
    clear_and_draw_fancy_face( "frown", 25, "(frown with big eyes)" )

    # test case 5:
    clear_and_draw_fancy_face( "smile", 35, "(smile with huge eyes)" )

    # test case 6:
    clear_and_draw_fancy_face( "frown", 15, "(frown with medium eyes)" )

    # leaves the last result up
    print( "end of tests." )

EYE_RADIUS_MIN = 0
EYE_RADIUS_MAX = 35

def prompt_and_draw_fancy_face():
    """
    prompt_and_draw_fancy_face prompts for the mouth type and the eye
    radius and draws an instance of the fancy face.
    """

    # bind the name mouth_type to the string value returned by input

    mouth_type = input ( "Enter mouth type (\"smile\" or \"frown\"): " )

    # convert string input to integer and bind name eye_radius to the value

    eye_radius = int( input( "Enter eye radius (a positive integer): " ) )

    # check the eye size is within limits
    if eye_radius >= EYE_RADIUS_MIN and eye_radius <= EYE_RADIUS_MAX:

        # pass the bound values in as arguments to another function

        init_world()
        clear_and_draw_fancy_face( mouth_type, eye_radius )
    else:
        print( "The eye radius", eye_radius, "is out of range[", \
                EYE_RADIUS_MIN, "-", EYE_RADIUS_MAX, "]" )


#
# top-level runtime content: if statement checking if this is a 'main' module.
# Python defined the string "__main__" when a user runs a module directly.
#
# Putting top-level execution in an if statement allows other python modules
# to import this module's definitions to suit its needs.
# Another module that imports this one might not want to run the same code.
#

if __name__ == "__main__":

    prompt_and_draw_fancy_face()
    answer = input( "Do you want to run the test cases too? (y or n) " )
    if answer == 'y' or answer == 'Y':
        run_test_cases()

    elif answer != 'N' and answer != 'n':
        print( "Error: '", answer, "' did not match requirements. exiting...")

    else:
        # question: can this else-block of code ever execute?
        print( "bye." )

    print( "Close the canvas window to end the program." )
    turtle.done()  