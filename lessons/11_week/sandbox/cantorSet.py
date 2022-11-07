#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python3 implementation to find the cantor set
# for n levels and
# for a given start_num and end_num
# The Linked List Structure for the Cantor Set
class Cantor:

    def __init__(self):

        self.start = 0;
        self.end = 0;
        self.next = None;

cantor = None;

# Function to initialize the Cantor Set List
def startList(head, start_num, end_num):

    if (head == None) :

        head = Cantor();
        head.start = start_num;
        head.end = end_num;
        head.next = None;

    return head;

# Function to propagate the list
# by adding new nodes for the next levels
def propagate(head):

    temp = head;

    if (temp != None):

        newNode = Cantor();
        diff = (((temp.end) - (temp.start)) / 3);

        # Modifying the start and end values
        # for the next level
        newNode.end = temp.end;
        temp.end = ((temp.start) + diff);
        newNode.start = (newNode.end) - diff;

        # Changing the pointers
        # to the next node
        newNode.next = temp.next;
        temp.next = newNode;

        # Recursively call the function
        # to generate the Cantor Set
        # for the entire level
        propagate(temp.next.next);

    return head;

# Function to Print a level of the Set
def Print(temp):

    while (temp != None) :

        print("[", temp.start, "] -- [", temp.end, "] ", sep = "", end = "");
        temp = temp.next;

    print()

# Function to build and display
# the Cantor Set for each level
def buildCantorSet(A, B, L):

    head = None;
    head = startList(head, A, B);
    for i in range(L):

        print("Level_", i, " : ", sep = "", end = "");
        Print(head);
        propagate(head);

    print("Level_", L, " : ", end = "", sep = "");
    Print(head);

# Driver code
A = 0;
B = 9;
L = 2;
buildCantorSet(A, B, L);

# This code is contributed by phasing17
# ref: https://www.geeksforgeeks.org/ternary-representation-of-cantor-set/
