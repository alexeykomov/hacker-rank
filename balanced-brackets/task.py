#!/bin/python

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def is_balanced(s):
    opening_to_closing = {
        '(':')',
        '{':'}',
        '[':']'
    }
    closing_to_opening = transpose(opening_to_closing)
    opened_brackets = []
    for char in s:
        print char
        if char in opening_to_closing:
            opened_brackets.append(char)
        elif char in closing_to_opening:
            if len(opened_brackets) and opened_brackets[-1] == closing_to_opening[char]:
                opened_brackets.pop()
            else:
                return 'NO'
    if len(opened_brackets):
        return 'NO'
    return 'YES'


def transpose(dict):
    transposed_dict = {}
    for key in dict:
        transposed_dict[dict[key]] = key
    return transposed_dict

if __name__ == '__main__':

    t = int(raw_input())

    for t_itr in xrange(t):
        s = raw_input()

        result = is_balanced(s)
        print result
