import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    swap=0
    for i,num in enumerate(arr):
        if num != i+1:
            i_swap=arr.index(i+1)
            arr[i],arr[i_swap]=arr[i_swap],arr[i]
            swap +=1
    return swap


    # this code works but times out for some test runs
    # working on optimizing
    # swap=0
    # current=0
    # for i,num in enumerate(arr):
        
    #     if num != i+1:
    #         current =num
    #         i_swap=arr.index(i+1)
    #         arr[i]=arr[i_swap]
    #         arr[i_swap]=current
    #         swap +=1
    # return swap

    