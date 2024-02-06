#!/bin/python3

import math
import os
import random
import re
import sys

class DB:
    def __init__(self):
        self.gmail_list = []
        self.rgx = "^.+@gmail.com"
    
    def add(self, firstName, emailID):
        if re.search(self.rgx, emailID):
            self.gmail_list.append(firstName)
    
    def print_gmail(self):
        self.gmail_list.sort()
        for e in self.gmail_list:
            print(e)
        

if __name__ == '__main__':
    N = int(input().strip())
    
    my_db = DB()
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        my_db.add(firstName, emailID)
    
    my_db.print_gmail()
        
