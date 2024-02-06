#!/bin/python3

import math
import os
import random
import re
import sys

def max_hourglass_sum(arr):
    mhgs = -math.inf
    for idx in range(4):
        for idy in range(4):
            hgs = hourglass_sum(arr, idx, idy)
            mhgs = max(mhgs, hgs)
    return mhgs

def hourglass_sum(arr, idx, idy):
    hgs = arr[idx][idy] + arr[idx][idy+1] + arr[idx][idy+2] +\
        arr[idx+1][idy+1] +\
        arr[idx+2][idy] + arr[idx+2][idy+1] + arr[idx+2][idy+2]
    return hgs

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    print(max_hourglass_sum(arr))
