#!/bin/python

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonal_difference(arr):
    left_to_right_diag_sum = 0
    right_to_left_diag_sum = 0

    for row_index in range(0, len(arr)):
        for col_index in range(0, len(arr[0])):
            if row_index == col_index:
                left_to_right_diag_sum += arr[row_index][col_index]
                right_col_index = len(arr) - col_index - 1
                right_to_left_diag_sum += arr[row_index][right_col_index]

    return abs(left_to_right_diag_sum - right_to_left_diag_sum)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonal_difference(arr)

    print result

    # fptr.write(str(result) + '\n')

    # fptr.close()
