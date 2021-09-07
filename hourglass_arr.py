import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    def hourglassSum(arr):
    
    #based off example negative numbers, give the highest sum a negative start
    #this is in case all numbers arnt positive
    highest_sum=-100
   
    #range goes to 4 because if it goes farther an hourglass is not made
    for i in range(0,4):
        for j in range(0,4):
            #these are the placements of an hourglass array
            hourglass_sum= (arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+
                            arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            
            #compare the current sum to the saved highest sum
            #if the current sum is greater, reassign the greatest sum
            #otherwise continue through the array
            if hourglass_sum > highest_sum:
                highest_sum=hourglass_sum
            else:
                continue
    
    return highest_sum

