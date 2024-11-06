"""
CSCI-141 Computer Science 1 Recitation
11-Linked Lists

Functions for working with mutable linked lists.
"""


def to_str(lst):
    """
    Construct a string that shows the contents of a linked list.
    The elements are separated by commas and surrounded by brackets.
    :param lst: The LinkedList whose contents will be printed
    """
    result = '['  # result is the accumulator
    node = lst.head
    while node is not None:
        result += ' ' + str(node.value)
        if node.next is not None:
            result += ','
        node = node.next
    result += ' ]'
    return result


def remove_value(lst, value):
    """
    Locate a value in a list and remove it.
    :param lst: the LinkedList object to be modified
    :param value: the value to search for, starting at head
    :except ValueError if the value is not found
    """
    node = lst.head
    if node is None:
        raise ValueError('No such value ' + str(value) + ' in list!')
    elif node.value == value:
        lst.head = node.next
    else:
        successor = node.next
        while successor is not None and successor.value != value:
            node = successor
            successor = node.next
        if successor is None:
            raise ValueError('No such value ' + str(value) + ' in list!')
        else:
            node.next = successor.next
    lst.size -= 1