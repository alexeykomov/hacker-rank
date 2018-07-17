#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plus_minus(arr):
    fractions = reduce(make_fractioner(len(arr)), arr, {
        'pos': 0,
        'neg': 0,
        'zero': 0
    })
    print fractions['pos']
    print fractions['neg']
    print fractions['zero']

def make_fractioner(length):
    def fraction(fractions, next):
        if next > 0:
            fractions['pos'] += 1.0 / length
        elif next < 0:
            fractions['neg'] += 1.0 / length
        else:
            fractions['zero'] += 1.0 / length

        return fractions
    return fraction

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plus_minus(arr)
