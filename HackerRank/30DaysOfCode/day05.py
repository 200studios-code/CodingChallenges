#!/bin/python3

import math
import os
import random
import re
import sys

def print_multiples(n, mult_num=10):
    for idx in range(1, mult_num+1):
        print(f'{n} x {idx} = {n*idx}')

if __name__ == '__main__':
    n = int(input().strip())
    print_multiples(n)
