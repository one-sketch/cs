"""
adder.py
James Heliotis
August 2017

Demonstrate use of a loop in an interactive setting.
"""

def adder1():
    print( "Enter numbers, one per line." )
    print( "Entering an empty line will cause the program to" )
    print( "display the sum of the entered numbers, then terminate." )
    print()

    sum = 0
    line = input( "> " )
    while line != "":
        number = float( line )
        sum = sum + number
        line = input( "> " )
    print( "The sum of the numbers entered is", sum )

def adder2():
    print( "Enter numbers, one per line." )
    print( "Entering an empty line will cause the program to" )
    print( "display the sum of the entered numbers, then terminate." )
    print()

    sum = 0
    while True:
        line = input( "> " )
        if line =="":
            break
        number = float( line )
        sum = sum + number
    print( "The sum of the numbers entered is", sum )

if __name__ == "__main__":
    adder2()
