"""
Fruitful functions.  Code for factorial and Fibonacci.

file: fruitful.py
language: python3
author: RIT CS Dept.
"""

def divide( num, denom) :
    """Return quotient of two numbers, rounded down to an integer.
       pre-condition: num, the dividend, is non-negative.
       pre-condition: denom, the divisor, is positive.
    """
    if num < denom:
        return 0
    else:
        # If (num - denom) / denom is q, (num / denom) must be q + 1
        return divide( num - denom, denom ) + 1

def fact( n) :
    """ Compute the factorial of a number.
        n should be non-negative.
    """
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def fib(n) :
    """ Compute the n-th Fibonacci number.
        n should be non-negative.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print("132 / 5 = ", divide(132,5))
    print("Recursive calculation of 35!  : ", fact(35))
    print("Recursive calculation of fib(35): ", fib(35))