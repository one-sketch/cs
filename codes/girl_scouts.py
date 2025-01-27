"""
This program introduces user-defined data structures using
dataclasses.  A dictionary of Girl Scout cookie orders is
read and analyzed.

File: girl_scouts.py
Author: CS @ rit.edu
"""

from dataclasses import dataclass

@dataclass
class BoxCount:
    """
    BoxCount represents a request for some number of a named cookie box.
    cookie is the name of the box.
    count is the number of those boxes.
    """
    cookie: str
    count: int

@dataclass
class Order:
    """
    Order represents an order of cookie boxes from a person.
    name is the name of the person.
    address is the address of the person.
    cost is the total cost of all the boxes in the order.
    paid is True if the order has been paid.
    cookies is the list of BoxCount items.
    """
    name: str
    address: str
    cost: float
    paid: bool
    cookies: list
                
def read_orders(filename):
    """
    Function to read cookie orders from input file.
    The file is assumed to have the following structure.
    It will be a multiple of 5 lines of data.  Each
    set of 5 lines represents a single order.
    Line 1: name
    Line 2: address
    Line 3: total cost
    Line 4: paid status
    Line 5: alphabetical listing of cookie varieties and counts,
    e.g. "Lemonades 1 ThinMints 2".  Cookie varieties are guaranteed
    to have no whitespace in the name.
    :param filename: name of input file
    :return: dictionary storing all orders
    """

    orders = {}

    with open(filename) as f:
        while True:
            line = f.readline().strip()
            if not line:    # same as checking if line == ""
                break
            name = line
            address = f.readline().strip()
            cost = float(f.readline())
            paid = f.readline().strip() == "True"
            cookies = []
            fields = f.readline().split()
            for loc in range(0, len(fields), 2):
                box = fields[loc]
                count = int(fields[loc + 1])
                cookies.append(BoxCount(box, count))
            order = Order(name, address, cost, paid, cookies)

            if name not in orders:
                orders[name] = order
            else:
                repeat_order(orders, order)

    return orders


def repeat_order(orders, order):
    """
    Handle case of repeat customer.  Assume address and
    paid status match for given name.  Need to update
    total cost and list of purchases.
    :param orders: current list of orders
    :param order: this order for a repeat customer
    :return: None.  The contents of the original
    customer order are augmented.
    """

    curr_order = orders[order.name]
    curr_order.cost += order.cost
    merge_lists(curr_order.cookies, order.cookies)

def merge_lists(list1, list2):
    """
    Merge two alphabetical lists of BoxCounts.
    list1 is modified to become the merged list.
    :param list1: first BoxCount list
    :param list2: second BoxCount list
    :return: None. list1 is modified to be the merged list.
    """
    idx1 = 0
    idx2 = 0
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1].cookie < list2[idx2].cookie:
            idx1 += 1
        elif list1[idx1].cookie == list2[idx2].cookie:
            list1[idx1].count += list2[idx2].count
            idx1 += 1
            idx2 += 1
        else:
            list1.insert(idx1, list2[idx2])
            idx1 += 1  # move idx1 past the element just inserted
            idx2 += 1

    if idx2 < len(list2):
        list1.extend(list2[idx2:])


def compute_box_totals(orders):
    """
    Function to compute the total number of boxes ordered
    of each type of cookie that has been ordered.
    :param orders: dictionary containing all orders
    :return: a dictionary mapping varieties of cookies
    that have been ordered to the total number of boxes
    requested of that cookie variety
    """

    totals = {}

    for order in orders.values():
        for box in order.cookies:
            if box.cookie not in totals:
                totals[box.cookie] = box.count
            else:
                totals[box.cookie] += box.count

    return totals


def main():
    orders = read_orders("orders.txt")
    for o in orders:
        print(orders[o])

    totals = compute_box_totals(orders)

    print("\nTotal Cookie Sales")
    for cookie in totals:
        print(cookie + ": " + str(totals[cookie]))


main()
