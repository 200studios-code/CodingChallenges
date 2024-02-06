#!/bin/python3

import math
import os
import random
import re
import sys

def solve(arr):
    out = ''
    for idx in range(len(arr)-1, -1, -1):
        out += f'{arr[idx]} '
    print(out)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    solve(arr)
