"""
file: dictionary_demo.py
description: demonstrates simple use of Python dictionary data type.
purpose: lecture example
author: bksteele
"""

def main():
    """
    main demonstrates simple use of Python dictionary data type.
    """

    print( "\n", "=" * 10, "Construction\n")

    print( "Create empty dictionary instances with dict() or {}.")
    d1 = dict()
    d2 = {}

    print( "\nOr populate a dictionary instance with a"
         , "sequence of <key> : <value> expressions inside {}."
         , "Example: d3 = { 'key1' : 'banana', 'key2' : 'apple' }", sep="\n")
    d3 = { 'key1' : 'banana', 'key2' : 'apple' }

    print( "\n", "=" * 10, "Inserts and Updates\n")

    d1['seafood'] = 'lobster'
    d1['horse food'] = 'hay'
    d1['dogfood'] = ['Rival']            # value type is a list
    d1['dogfood'].append( 'Puppy Chow')

    print( "d3 ", d3)
    d3['key2'] = "grape"
    print( "after update, d3 ", d3)

    print( "\n", "=" * 10, "Prints, Fetches and Queries\n")

    print( "d1 ", d1)
    print( "d2 ", d2)
    print( "d3 ", d3)

    print( "'key2' in d2", 'key2' in d2)

    d2[2] = 'two'
    print( "2 in d2", 2 in d2)
    print( "d2 ", d2)

    print( "'key2' in d3", 'key2' in d3)
    print( "value of 'key1' in d3:", d3['key1'])

    print( "\n", "=" * 10, "Deleting Entries\n")

    print( "'key2' in d3", 'key2' in d3)
    del d3['key2']
    print( "after deletion d3 has ", d3)

    print( "d1 ", d1)
    print( "d2 ", d2)
    print( "d3 ", d3)

    print( "\n", "=" * 10, "Iterating through Dictionaries\n")

    print( "d1: ")
    for key in d1:
        print( "key:", key, "value:", d1[key], sep="\t")

    print()

    for key in d1.keys():
        print( "key:", key)

if __name__ == "__main__":
    main()