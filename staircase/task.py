#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    delimeter = n - 1
    for row in range(0, n):
        acc = []
        for col in range(0, delimeter):
            acc.append(' ')
        for col in range(delimeter, n):
            acc.append('#')
        delimeter -= 1
        print ''.join(acc)

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
