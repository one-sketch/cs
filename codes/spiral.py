"""
spiral.py
author: Bobby St. Jacques
Fall 2018

Demonstrate drawing a spiral with tail recursion and iteration.
"""

import turtle

def draw_spiral(segments):
    """ Draws a spiral using tail recursion.
        :param segments: The number of segments in the spiral. Also the
                         length of the next segment.
        :preconditions: segments must be non-negative.
    """
    if segments == 0:
        pass
    else:
        turtle.forward(segments)
        turtle.right(90)
        draw_spiral(segments -1)

def draw_spiral_iter( segments ):
    """ Draws a spiral using iteration.
        :param segments: The number of segments in the spiral. Also the length
                         of the longest segment.
        :preconditions: segments must be greater than or equal to 0
    """
    while True:
        if segments == 0:
            break
        else:
            turtle.forward(segments)
            turtle.right(90)
            segments = segments - 1

def draw_spiral_simple( segments ):
    """ Draws a spiral using simplified iteration.
        :param segments: The number of segments in the spiral. Also the length
                         of the longest segment.
        :preconditions: segments must be greater than or equal to 0
    """
    while segments != 0:
        turtle.forward(segments)
        turtle.right(90)
        segments = segments - 1

def main():
    turtle.speed(0)

    turtle.color("green")
    turtle.penup()
    turtle.back(200)
    turtle.left(90)
    turtle.pendown()
    draw_spiral(50)
    
    turtle.color("blue")
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    draw_spiral_iter(100)
    turtle.penup()
    turtle.forward(100)

    turtle.pendown()
    turtle.color("orange")
    draw_spiral_simple(150)
    turtle.done()

if __name__ == "__main__":
    main()