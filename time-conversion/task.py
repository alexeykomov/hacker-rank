#!/usr/bin/python

import os
import sys

#
# Complete the timeConversion function below.
#
def time_conversion(s):
    hours12format = s[0:2]
    hours24fformat = hours12format
    if hours12format[0] == '0':
        hours24format = str(int(hours12format[1]) + 12)
    date24format = hours24format + s[2:8]

    return date24format

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = time_conversion(s)
    print result

    # f.write(result + '\n')

    # f.close()
