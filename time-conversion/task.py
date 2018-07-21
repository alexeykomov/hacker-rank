#!/usr/bin/python

import os
import sys

#
# Complete the timeConversion function below.
#
def time_conversion(s):
    hours12format = s[0:2]
    hours24format = hours12format
    if s[8:10] == 'AM' and s[0:2] == '12':
        hours24format = '00'
    if s == '12:00:00PM':
        return '12:00:00'
    if s[8:10] == 'PM' and int(s[0:2]) < 12:
        hours24format = str(int(hours12format) + 12)
    date24format = hours24format + s[2:8]

    return date24format

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = time_conversion(s)
    print result

    # f.write(result + '\n')

    # f.close()
