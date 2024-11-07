""" 
combo_tree.py draws a tree of trees by combining functions.

assignment: lecture
language: python3
author: bksteele
"""

import turtle as tt

# definitions

def init_world( size ):
    """
    init_world initializes the drawing canvas.

    size -- PositiveNumber; scales the canvas for fitting the size.

    post-conditions: canvas size is 600px x 600px
                     coordinate system is
                     from (-2*|size|,-2*|size|) at lower-left
                       to (2*|size|, 2*|size|) at upper-right, and
                     turtle is at origin, and
                     turtle is facing North, and
                     turtle is pen-down.
    """
    tt.setup( 600, 600 )
    reset_world( size )


def reset_world( size ):
    """
    reset_world initializes the drawing but does not resize the window.

    size -- PositiveNumber; scales the canvas for fitting the size.

    post-conditions: coordinate system is
                     from (-2*|size|,-2*|size|) at lower-left
                       to (2*|size|, 2*|size|) at upper-right, and
                     turtle is at origin, and
                     turtle is facing North, and
                     turtle is pen-down.
    """
    # provide canvas boundary of 2
    tt.setworldcoordinates( -2 * abs( size ) - 2, -2 * abs( size ) - 2,
                            2 * abs( size ) + 2, 2 * abs( size ) + 2 )
    tt.clear()
    tt.setheading( 90 )  # turtle is facing North
    tt.down()  # turtle is pen-down
    tt.pensize( 2 )


def draw_tree0( size ):
    """
    draw_tree0 draws a 0-level tree (i.e., a seed).

    size -- PositiveNumber; length of trunk should be positive.

    returns: 0 because the seed has 0 size

    pre-conditions: size > 0, and
                    turtle is at base of tree, and
                    turtle is facing along trunk of tree, and
                    turtle is pen-down.
    post-conditions: a 0-level tree was drawn on the canvas, and
                     turtle is at base of tree, and
                     turtle is facing along trunk of tree, and
                     turtle is pen-down.
    """
    return 0     # drew nothing


def draw_tree1( size ):
    """
    draw_tree1 draws a 1-level tree (i.e., a tree trunk)

    size -- PositiveNumber; length of tree trunk should be positive.

    returns: sum of sizes of all trunks and branches

    pre-conditions: size > 0, and
                    turtle is at base of tree, and
                    turtle is facing along trunk of tree, and
                    turtle is pen-down.
    post-conditions: a tree was drawn on the canvas, and
                     turtle is at base of tree, and
                     turtle is facing along trunk of tree, and
                     turtle is pen-down.
    """
    tt.forward( size )
    total = size + draw_tree0( size/2 )
    tt.forward( -size )
    return total


def draw_tree2( size ):
    """
    draw_tree2 draws a Y-tree on a tree (trunk).

    size -- PositiveNumber; length of trunk should be positive.

    returns: sum of sizes of all trunks and branches

    pre-conditions: size > 0, and
                    turtle is at base of tree, and
                    turtle is facing along trunk of tree, and
                    turtle is pen-down.
    post-conditions: a 2-level tree was drawn on the canvas,
                     turtle is at base of tree, and
                     turtle is facing along trunk of tree, and
                     turtle is pen-down.
    """
    # draw trunk and two sub-trees
    tt.forward( size )
    tt.left( 45 )
    leftside = draw_tree1( size/2 )
    #draw_tree1( size / 2 )
    tt.right( 90 )
    rightside = draw_tree1( size/2 )
    tt.left( 45 )
    tt.forward( -size )
    return size + leftside + rightside


def draw_tree3( size ):
    """
    draw_tree3 draws a Y-tree on a Y-tree on a tree.

    size -- PositiveNumber; length of trunk should be positive.

    returns: sum of sizes of all trunks and branches
    pre-conditions: size > 0, and 
                    turtle is at base of tree, and
                    turtle is facing along trunk of tree, and
                    turtle is pen-down.
    post-conditions: a 3-level tree was drawn on the canvas, and
                     turtle is at base of tree, and
                     turtle is facing along trunk of tree, and
                     turtle is pen-down.
    """
    # draw trunk and two sub-trees
    tt.forward( size )
    tt.left( 45 )
    leftside = draw_tree2( size/2 )
    tt.right( 90 )
    rightside = draw_tree2( size/2 )
    tt.left( 45 )
    tt.forward( -size )
    return size + leftside + rightside



def draw_tree4( size ):
    """
    draw_tree4 draws a Y-tree on a Y-tree on a Y-tree on a tree.

    size -- PositiveNumber; length of trunk should be positive.

    returns: sum of sizes of all trunks and branches
    pre-conditions: size > 0, and 
                    turtle is at base of tree, and
                    turtle is facing along trunk of tree, and
                    turtle is pen-down.
    post-conditions: a 4-level tree was drawn on the canvas, and
                     turtle is at base of tree, and
                     turtle is facing along trunk of tree, and
                     turtle is pen-down.
    """
    # draw trunk and two sub-trees
    tt.forward( size )
    tt.left( 45 )
    leftside = draw_tree3( size/2 )
    tt.right( 90 )
    rightside = draw_tree3( size/2 )
    tt.left( 45 )
    tt.forward( -size )
    return size + leftside + rightside



def reset_world_and_draw_tree( levels, size, message="" ):
    """
    init_world_and_draw_tree prints a message, initializes the world,
    draws an instance of the tree of trees, and waits for ENTER.

    levels -- NonNegativeInteger;
                number of levels from the base of the tree to
                the end of any branch should be integral and non-negative.
    size -- PositiveNumber; length of trunk should be positive.
    message -- String;
               message to display
    """
    print( "Drawing tree :", (levels, size), ";", message )
    reset_world( size )

    # make the appropriate call based on the level count
    if levels == 4:
        total = draw_tree4( size )
    elif levels == 3:
        total = draw_tree3( size )
    elif levels == 2:
        total = draw_tree2( size )
    elif levels == 1:
        total = draw_tree1( size )
    else:
        total = draw_tree0( size )

    print( "Total tree length is", total)
    input( "Hit ENTER to continue ")


def run_test_cases():
    """
    Execute test cases for each level.
    """
    init_world( 100 )

    # test case 1: levels=0, size=100
    reset_world_and_draw_tree( 0, 100, "(seed, turtle image)" )

    # test case 2: levels=1, size=50
    reset_world_and_draw_tree( 1, 50,
        "(tree trunk, trunk == 50)" )

    # test case 3: levels=2, size=100
    reset_world_and_draw_tree( 2, 100,
        "(Y-trees on a tree trunk, trunk == 100)" )

    # test case 4: levels=3, size=100
    reset_world_and_draw_tree( 3, 100,
        "(Y-trees on Y-trees on a tree trunk, trunk == 100)" )

    # test case 5: levels=4, size=100
    reset_world_and_draw_tree( 4, 100,
        "(Y-trees on Y-trees on Y-trees on a tree trunk, trunk == 100)" )


# script execution/run

if __name__ == "__main__":
    run_test_cases()
    print( "close the window to quit")
    tt.done()
