#!/bin/python3

import math
import os
import random
import re
import sys

def solve(N):
    if N % 2 == 1:
        print('Weird')
    else:
        if N < 5:
            print('Not Weird')
        elif N < 21:
            print('Weird')
        else:
            print('Not Weird')

if __name__ == '__main__':
    N = int(input().strip())
    solve(N)
