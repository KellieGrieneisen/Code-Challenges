#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    
    # First round
    # count=0
    # for i,word in enumerate(note):
    #     if magazine.count(word) == note.count(word) and magazine.index(word) >= i:
    #         count +=1
    # if count == len(note):
    #     print("Yes")
    # else:
    #     print("No")

    # Second round
    # check=[]
    # for word in note:
    #     if word in str(magazine) and magazine.count(word) == note.count(word):
    #         check.append(word)
    # if ''.join(check) == ''.join(note):
    #     print("Yes")
    # else:
    #     print("No")

    check=[]
    for word in magazine:
        if word in note:
            check.append(word)
    if ''.join(check) == ''.join(note):
        print("Yes")
    else:
        print("No")
        
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)