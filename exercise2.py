#!/bin/python3

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
    
    total_sum = []
    sum = 0
    
    for i in range(1, 5):
        for j in range (1, 5):
            top = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            middle = arr[i][j]
            bottom = arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            
            hourglass = top + middle + bottom
            
            total_sum.append(hourglass)
            max_sum = max(total_sum)
    return max_sum
    
    for n in total_sum:
        sum +=n
                
    return sum
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
