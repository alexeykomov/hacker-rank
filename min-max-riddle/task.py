#!/bin/python

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    # complete this function

def get_next_smaller(elements):
    stack = []
    pairs = {}

    if len(elements):
        stack.append(elements[0])
    for counter in range(1, len(elements)):
        next = elements[counter]
        if len(stack):
            element = stack.pop()

            while element < next:
                pairs[element] = next
                if not len(stack):
                    break
                element = stack.pop()

            if element > next:
                stack.append(element)

    while len(stack):
        element = stack.pop()
        pairs[element] = -1

    return pairs;


if __name__ == '__main__':
    n = int(raw_input())

    arr = map(long, raw_input().rstrip().split())

    res = get_next_smaller(arr)
