"""
factorial.py
James Heliotis, Bobby St. Jacques
Fall 2018

Demonstrate tail-recursive and iterative solutions to the factorial function.
"""

def factorial( number ):
    """ Compute the factorial of a number using general recursion.
        :param number: The number for which Factorial is to be computed.
        :preconditions: number is non-negative
    """
    if number == 0:
        return 1
    else:
        return number * factorial( number - 1 )

##########################################################################

def factorial_accum(number, accumulator=1):
    """ Computes the factrial for a given number using tail recursion.
        "Private" function not meant to be called directly.
        :param number: The number for which facorial should be computed.
        :param accumulator: The accumulator used to hold the result so far.
        :preconditions: number is greater than or equal to 0.
    """
    if number == 0:
        # we are done; return the accumulated result
        return accumulator
    else:
        # use the accumulator to compute one part
        accumulator = number * accumulator
        # pass it into the recursive call
        return factorial_accum( number - 1, accumulator )


def factorial_user(number):
    """ Computes the factrial for a given number using tail recursion.
        "Public" function that doesn't require the caller to provide an
        initial value for the accumulator.
        :param number: The number for which factorial should be computes.
    """ 
    return factorial_accum(number, 1)

##########################################################################

def factorial_loop(number):
    """ Computes the factorial for a given number using a while loop.
        param n: The number for which factorial should be computed.
        :pre: n is non-negative
        This algorithm is not recursive; it uses a while loop.
    """
    accumulator = 1 # the accumulator
    while number > 0:
        accumulator = accumulator * number
        number = number - 1
    return accumulator


def test_factorials():
    number = 0
    while number <= 15:
        print(number, ":",
              factorial(number),
              factorial_accum(number),
              factorial_user(number),
              factorial_loop(number))
        number = number + 1


if __name__ == "__main__":
    test_factorials()