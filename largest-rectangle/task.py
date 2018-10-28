#!/bin/python

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largest_rectangle(hist):
    stack = []
    max_area = -1


    for rectangle_counter in range(0, len(hist)):
        if len(stack) == 0 or stack[-1] < hist[rectangle_counter]:
            stack.append(hist[rectangle_counter])
        else:
            while stack[-1] > hist[rectangle_counter]:
                top


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    h = map(int, raw_input().rstrip().split())

    result = largest_rectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
