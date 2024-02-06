#!/bin/python3

import math
import os
import random
import re
import sys

def swap(arr, idx, jdx):
    tmp = arr[idx]
    arr[idx] = arr[jdx]
    arr[jdx] = tmp

def perform_sorting(arr, n):
    total_swaps = 0
    for idx in range(n):
        num_swaps = 0
        for jdx in range(n-1):
            if arr[jdx] > arr[jdx+1]:
                swap(arr, jdx, jdx+1)
                num_swaps += 1
        total_swaps += num_swaps
        if num_swaps == 0:
            break
    
    print(f'Array is sorted in {total_swaps} swaps.')
    print(f'First Element: {arr[0]}')
    print(f'Last Element: {arr[n-1]}')
        

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    perform_sorting(a, n)
