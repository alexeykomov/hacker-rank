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
    top = 0

    for rectangle_counter in range(0, len(hist)):
        if len(stack) == 0 or hist[stack[-1]] < hist[rectangle_counter]:
            stack.append(rectangle_counter)
        else:
            while len(stack) and hist[stack[-1]] > hist[rectangle_counter]:
                top = stack.pop()
                area = hist[top] * (rectangle_counter - top - 1)
                if area > max_area:
                    max_area = area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    h = map(int, raw_input().rstrip().split())

    result = largest_rectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
