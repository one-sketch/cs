"""
file: find_lengths.py
language: python3
author: ben k steele, bks@cs.rit.edu
description: print the length of a sentence and its longest word.
date: 07/2017
purpose: strings lecture
"""

import lengths

def main():
    """
    main prompts for a sentence, finds the longest word in the input, and
    prints the length.
    """
    print( "Length of sentence and longest 'word' or non-whitespace sequence")
    sentence = input( "Enter a sentence to search ")
    print( "Sentence length:", lengths.length( sentence))
    print( "Longest length:", lengths.longest( sentence))

if __name__ == "__main__": # run tests in this case
    main()
