#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes=0
    
    for rider in range(0,len(q)):
     
        if (q[rider]-1)-rider >2:
            return(print("Too chaotic"))
            
        else:
            for i in range(rider,len(q)):
                if q[rider] > q[i]:
                    bribes+=1
            
                   
    print (bribes)