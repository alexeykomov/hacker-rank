#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthday_cake_candles(ar):
    current_max = 0
    number_of_current_max = 0

    for candle in ar:
        if candle > current_max:
            current_max = candle
            number_of_current_max = 1
        elif candle == current_max:
            number_of_current_max += 1

    return number_of_current_max

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = birthday_cake_candles(ar)

    print result
