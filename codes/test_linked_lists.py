"""
CSCI-141 Computer Science 1 Recitation
11-Linked Lists

Tester for immutable and mutable lists.
"""

from immutable_list import append, insert_before_index
from mutable_list import to_str, remove_value
from linked_list_type import LinkedList, make_empty_list
from nodes_types import MutableNode


def test_append():
    """Run all tests on append"""
    print('testing append...')
    head = None
    head = append(head, 'A')
    print('append A:', head)
    head = append(head, 'B')
    print('append B:', head)
    head = append(head, 'C')
    print('append C:', head)


def test_insert_before_index():
    """Run all tests on insert_before_index"""
    print('\ntesting insert_before_index...')
    head = None
    head = insert_before_index(head, 'B', 0)
    print('insert B at 0:', head)
    head = insert_before_index(head, 'D', 1)
    print('insert D at 1:', head)
    head = insert_before_index(head, 'E', 2)
    print('insert E at 2:', head)
    head = insert_before_index(head, 'C', 1)
    print('insert C at 1:', head)
    head = insert_before_index(head, 'A', 0)
    print('insert A at 0:', head)


def test_immutable_lists():
    """Run all tests on immutable lists"""
    test_append()
    test_insert_before_index()


def test_to_str():
    """Run all tests on to_str"""
    print('\ntesting to_str...')
    lst = make_empty_list()
    print('empty list:', to_str(lst))

    lst.head = MutableNode('A', MutableNode('B', MutableNode('C', None)))
    print('three element list:', to_str(lst))


def test_remove_value():
    """Run all tests for remove_value"""
    print('\ntesting remove_value...')

    lst = make_empty_list()
    lst.head = MutableNode('A', MutableNode('B', MutableNode('C', None)))
    print('initial list:', to_str(lst))

    remove_value(lst, 'B')
    print('remove B:', to_str(lst))

    remove_value(lst, 'A')
    print('remove A:', to_str(lst))

    remove_value(lst, 'C')
    print('remove C:', to_str(lst))

    lst = make_empty_list()
    try:
        remove_value(lst, 'A')
    except ValueError as e:
        print(e)

    lst.head = MutableNode('A', MutableNode('B', MutableNode('C', None)))
    try:
        remove_value(lst, 'X')
    except ValueError as e:
        print(e)


def test_mutable_lists():
    """Run all mutable list tests"""
    test_to_str()
    test_remove_value()


def run_tests():
    """Run all tests on immutable and mutable lists"""
    test_immutable_lists()
    test_mutable_lists()

if __name__ == '__main__':
    run_tests()