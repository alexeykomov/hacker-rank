#!/bin/python

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def two_strings(s1, s2):
    s1chars = {}
    for char in s1:
        s1chars[char] = True
    for char in s2:
        if char in s1chars:
            return 'YES'
    return 'NO'

if __name__ == '__main__':

    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = two_strings(s1, s2)

        print result
