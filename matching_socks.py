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
    
    for i,num in enumerate(ar):
        count = ar.count(num)
        if num not in seen:
            pairs.append(math.floor(count/2))
        seen.append(ar.pop(i))
        
            
        
    return sum(pairs)
                
                
                
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
