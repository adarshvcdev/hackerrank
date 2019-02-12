#!/bin/python3

import math
import os
import random
import re
import sys

def get_smallest_stick(arr):
    x = min(float(s) for s in arr)
    return x

def cutTheSticks(arr):
    least = get_smallest_stick(arr)
    cut_count = 0
    new_array = []
    for item in arr:
        x = item - least
        cut_count = cut_count + 1        
        if x > 0:
            new_array.append(x)    
       
    return (new_array, cut_count)

# Complete the cutTheSticks function below.
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = []

    while(len(arr) > 0):
        arr,cut_count = cutTheSticks(arr)
        result.append(cut_count)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

