# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys

def before_due_date(days_diff, month_diff, year_diff):
    return year_diff > 0 or (year_diff == 0 and month_diff > 0) or (year_diff == 0 and month_diff == 0 and days_diff >= 0)
    
def same_month_and_year(month_diff, year_diff):
    return month_diff == 0 and year_diff == 0

def same_year(year_diff):
    return year_diff == 0

def calculate_fine(dr, mr, yr, dd, md, yd):
    days_diff = dd - dr
    month_diff = md - mr
    year_diff = yd - yr

    # Can you find a simpler solution by rearranging the conditionals? (Hint: check year first, then month, then days)
    if before_due_date(days_diff, month_diff, year_diff):
        return 0
    elif same_month_and_year(month_diff, year_diff):
        return 15 * -days_diff
    elif same_year(year_diff):
        return 500 * -month_diff
    else:
        return 10000

if __name__ == '__main__':
    # Received
    dr, mr, yr = map(int, input().split())
    # Due
    dd, md, yd = map(int, input().split())
    
    print(calculate_fine(dr, mr, yr, dd, md, yd))
