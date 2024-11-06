"""
CSCI-141 Computer Science 1 Recitation
11-Linked Lists

Functions for working with immutable linked lists.
"""

from nodes_types import FrozenNode


def append(head, new_value):
    """
    Effectively place a new value at the end of a list.
    :param head: the head of the original list
    :param new_value: the value with which to append the list
    :return: a new list containing all of head's values, plus new_value
    """
    if head is None:
        return FrozenNode(new_value, None)
    else:
        return FrozenNode(head.value, append( head.next, new_value ))

def insert_before_index(head, new_value, index):
    """
    Effectively stick a new value in front of the node at a certain ordinal
    position in a list.
    Note that this implementation creates a list that shares any nodes beyond
    the insertion point. That is not a problem because the nodes are immutable.
    :param head: the head of the given list
    :param new_value: the new value to be inserted
    :param index: how far down, starting at head being index 0, to insert
                  the new value. Everything at the given index and later
                  is effectively shifted further down,
    :except ndexError if index out of range
    :return: the head of the new list containing all the old values plus
             new_value in the proper place.
    :pre: 0 <= index <= length of list
    """
    if index == 0:
        # Note: this case has two perspectives:
        # (1) We are past the end of the list; (2) We are given an empty list.
        return FrozenNode(new_value, head)
    elif head is None:  # index > 0
        raise IndexError('List is shorter than index ' + str( index ) + '!')
    else:
        return FrozenNode(
            head.value,
            insert_before_index(head.next, new_value, index - 1)
        )