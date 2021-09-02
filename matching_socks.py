import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs=[]
    seen=[]
    count=0
    x=0   
    while x in range(0,len(ar)):
        for num in ar:
            count = ar.count(num)
      
            if num not in seen:
                pairs.append(math.floor(count/2))
                seen.append(num)
            x=x+1
            
            if x==len(ar):
                return sum(pairs)
        
    return sum(pairs)
                
                
                
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
