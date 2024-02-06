# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys

def is_prime(n):
    if n == 2:
        return 'Prime'
    if n == 1 or n % 2 == 0:
        return 'Not prime'
    for ix in range(3, int(math.sqrt(n))+1, 2):
        if n % ix == 0:
            return 'Not prime'
    return 'Prime'

if __name__ == '__main__':

    tests = int(input())

    for _ in range(tests):
        n = int(input())
        print(is_prime(n))
