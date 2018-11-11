#!/bin/python

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    # complete this function
    pass

def is_smaller(a, b):
    return a < b

def is_greater(a, b):
    return a > b

def get_next_smaller(elements, next):
    stack = []
    pairs = {}

    if len(elements):
        if next:
            stack.append(elements[0])
        else:
            stack.append(elements[-1])
    if next:
        direction = range(1, len(elements))
    else:
        direction = range(len(elements) - 2, -1, -1)

    for counter in direction:
        next = elements[counter]
        if len(stack):
            element = stack.pop()

            while is_greater(element, next):
                pairs[element] = next
                if not len(stack):
                    break
                element = stack.pop()

            if is_smaller(element, next):
                stack.append(element)

        stack.append(next)

    while len(stack):
        element = stack.pop()
        pairs[element] = -1

    return map(lambda element: pairs[element], elements)


if __name__ == '__main__':
    n = int(raw_input())

    arr = map(long, raw_input().rstrip().split())

    res = get_next_smaller(arr, True)
    res_prev = get_next_smaller(arr, False)

    print 'res: ' + str(res)
    print 'res: ' + str(res_prev)