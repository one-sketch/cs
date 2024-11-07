import turtle

def draw(level,sz):
    turtle.forward(2*sz)
    turtle.back(2*sz)
    turtle.circle(sz)
    turtle.right(90)
    if level > 1:
        draw(level-1,sz/2)

def draw_iter(level,sz):
    pass

def sum_even_squares(n):
    pass

def print_triangle(n):
    pass
