#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    counts = [0] * k
    for num in s:
        counts[num % k] += 1

    result = min(counts[0], 1)

    upper = (k // 2) if (k % 2 == 0) else (k // 2 + 1)
    for i in range(1, upper):
        result += max(counts[i], counts[k - i])

    
    if k % 2 == 0:
        result += min(counts[k // 2], 1)

    return result
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
