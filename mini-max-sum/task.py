#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def mini_max_sum(arr):
    sums = []
    for counter in range(0, len(arr)):
        next_sum = []
        for counter_left in range(0, counter):
            next_sum.append(arr[counter_left])
        for counter_right in range(counter + 1, len(arr)):
            next_sum.append(arr[counter_right])
        sums.append(sum(next_sum))
    print str(min(sums)) + ' ' + str(max(sums))

def make_sum_with_exception(index_to_omit):
    def sum_with_exception(acc, next):
        pass
    return

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    mini_max_sum(arr)
