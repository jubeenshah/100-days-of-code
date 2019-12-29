#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(h1, h2):
    if not h1 or not h2:
        return h1 or h2

    head, h1, h2 = (h1, h1.next, h2) if min([h1.data, h2.data]) == h1.data else (h2, h1, h2.next)
    curr = head
    while h1 or h2:

        if not h1 or not h2:
            curr.next = h1 or h2
            return head

        curr.next, h1, h2 = (h1, h1.next, h2) if min([h1.data, h2.data]) == h1.data else (h2, h1, h2.next)
        curr = curr.next
    return head

        

if __name__ == '__main__':