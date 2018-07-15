#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    alice_score = 0
    bob_score = 0
    for score_index in range(0, 3):
        if a[score_index] > b[score_index]:
            alice_score += 1
        elif a[score_index] < b[score_index]:
            bob_score += 1
    return [alice_score, bob_score]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = solve(a, b)


    output = ' '.join(map(str, result))
    print output

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
