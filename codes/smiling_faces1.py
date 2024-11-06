"""
   Use turtle graphics to draw a simple face.

   file: smiling_faces1.py
   author: RIT CS Dept.
"""

# imports the turtle module which draws pictures on a canvas window.

import turtle

# definitions of functions and procedures

def draw_border():
    """
        Draw a circle for the outline of the face.
        :precondition: Turtle is pointing towards the center of the face.
        :precondition: Turtle's pen is up.
        :postcontion: Turtle's state is the same as at start of the function.
    """
    turtle.right( 90 )
    turtle.down()
    turtle.circle( 100 )
    turtle.up()
    turtle.left( 90 )

def draw_mouth():
    """
        Draw a smiling mouth 60 points wide (30 units per side),
        40 points above the bottom of the face.
        :precondition: Turtle is pointing towards the center of the face.
        :precondition: Turtle's pen is up.
        :postcontion: Turtle's state is the same as at start of the function.
    """
    turtle.forward( 40 )
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
    turtle.forward( 40 )
    turtle.left( 180 )

def draw_nose():
    """
        Draw a nose as an equilateral triangle with sides of 30,
        70 points above the bottom of the face.
        :precondition: Turtle is pointing towards the center of the face.
        :precondition: Turtle's pen is up.
        :postcontion: Turtle's state is the same as at start of the function.
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

def draw_eyes():
    """
        Draw both eyes as circles of radius 15, 100 points above the bottom
        of the face, and with centers 100 points apart.
        :precondition: Turtle is pointing towards the center of the face.
        :precondition: Turtle's pen is up.
        :postcontion: Turtle's state is the same as at start of the function.
    """
    turtle.forward( 100 )
    turtle.left( 90 )
    turtle.forward( 50 )
    turtle.right( 180 )
    draw_eye()
    turtle.forward( 100 )
    draw_eye()
    turtle.right( 180 )
    turtle.forward( 50 )
    turtle.left( 90 )
    turtle.forward( 100 )
    turtle.left( 180 )

def draw_eye():
    """
        Draw a single eye as a 15-point-radius circle.
        Assume the turtle is facing right at the bottom of where the
        eye will be. Leave the turtle in that same state.
        :precondition: Turtle is pointing towards the center of the face.
        :precondition: Turtle's pen is up.
        :postcontion: Turtle's state is the same as at start of the function.
    """
    turtle.down()
    turtle.circle( 15 )
    turtle.up()

def draw_face():
    """
        Draw a smiling face.
    """
    draw_border()
    draw_mouth()
    draw_nose()
    draw_eyes()

def initialize():
    """
        Initialize the turtle so that it is facing North with the pen up.
        :postcondition: Turtle is pointing towards the center of the face.
        :postcondition: Turtle's pen is up.
    """
    turtle.up()
    turtle.left( 90 )
    turtle.pensize( 2 )

def main():
    """ The program creates a picture canvas, draws a smiling face,
       waits for user input, draws another face (the reflection), and
       prints instructions to close the canvas window to end the program.
    """
    initialize()
    draw_face()
    print( "Click on the close button (X) of the canvas to end the program." )
    turtle.done()
    print( "Have a nice day!")
	

# now call the main function to run the program code

main()