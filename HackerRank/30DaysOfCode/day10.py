#!/bin/python3

import math
import os
import random
import re
import sys

def max_consecutive_ones(n):
    max_ones = 0
    ones = 0
    while n>0:
        cur_bit = n % 2 == 1
        if cur_bit:
            ones += 1
        else:
            max_ones = max(max_ones, ones)
            ones = 0
        n >>= 1
    max_ones = max(max_ones, ones)
    return max_ones

if __name__ == '__main__':
    n = int(input().strip())
    print(max_consecutive_ones(n))
