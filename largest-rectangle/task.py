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

    for counter in range(0, len(hist)):
        if len(stack) == 0 or hist[stack[-1]] <= hist[counter]:
            stack.append(counter)
        else:
            while len(stack) and hist[stack[-1]] >= hist[counter]:
                top = stack.pop()
                if len(stack)пые:
                    area = hist[top] * (counter - stack[-1] - 1)
                else:
                    area = hist[top] * counter
                if area > max_area:
                    max_area = area
            stack.append(counter)

    while len(stack):
        top = stack.pop()
        if len(stack):
            area = hist[top] * (len(hist) - stack[-1] - 1)
        else:
            area = hist[top] * len(hist)
        if area > max_area:
            max_area = area

    return max_area


if __name__ == '__main__':

    n = int(raw_input())

    h = map(int, raw_input().rstrip().split())

    result = largest_rectangle(h)

    print result
