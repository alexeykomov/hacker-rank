#!/bin/python

import math
import os
import random
import re
import sys

def is_smaller(a, b):
    return a < b

def is_greater(a, b):
    return a > b

def is_smaller_or_equal(a, b):
    return a <= b

def is_greater_or_equal(a, b):
    return a >= b

def get_next_smaller(elements, forward):
    stack = []
    pairs = {}

    # We're searching for next smaller, not the next greater.
    # So we need to swap compare functions from this example
    # https://www.geeksforgeeks.org/next-greater-element/
    compare = is_greater
    compare_inverse = is_smaller_or_equal

    if len(elements):
        if forward:
            stack.append([elements[0], 0])
        else:
            stack.append([elements[-1], len(elements) - 1])
    if forward:
        direction = range(1, len(elements))
    else:
        direction = range(len(elements) - 2, -1, -1)

    for counter in direction:
        next = elements[counter]
        if len(stack):
            element, index = stack.pop()

            while compare(element, next):
                pairs[index] = counter
                if not len(stack):
                    break
                element, index = stack.pop()

            if compare_inverse(element, next):
                stack.append([element, index])

        stack.append([next, counter])

    while len(stack):
        element, index = stack.pop()
        if forward:
            pairs[index] = len(elements)
        else:
            pairs[index] = -1

    return map(lambda index: pairs[index], range(0, len(elements)))

def get_max_for_window_sizes(elements):
    next_smallers = get_next_smaller(arr, True)
    prev_smallers = get_next_smaller(arr, False)

    window_maxs = [0] * (len(elements) + 1)
    for counter in range(0, len(elements)):
        length = next_smallers[counter] - prev_smallers[counter] - 1

        window_maxs[length] = max(elements[counter], window_maxs[length])

    for length in range(len(elements) - 1, 1, -1):
        window_maxs[length] = max(window_maxs[length], window_maxs[length + 1])
    return window_maxs[1:]


if __name__ == '__main__':
    n = int(raw_input())

    arr = map(long, raw_input().rstrip().split())

    window_maxs = get_max_for_window_sizes(arr)

    print window_maxs

