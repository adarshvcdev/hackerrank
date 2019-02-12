#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def num_not_in_limit(i,x):
    diff = abs(i - x)
    print('i = ' + str(i) + ' x = ' + str(x) + ' diff - ' + str(diff))
    if diff > 1:
        return True
    else:
        return False


def is_num_quailified_with(arr, x):
    if len(arr) == 0:
        return True        
    for i in arr:
        if num_not_in_limit(i,x):
            return False
    return True    
        

def pickingNumbers(a):    
    main_list = []    
    for ind, y in enumerate(a):
        sub_list = [y]
        for idx, x in enumerate(a):
            if idx != ind:
                if is_num_quailified_with(sub_list, x):
                    sub_list.append(x)            
        main_list.append(sub_list)
    max_len = 0
    
    for ls in main_list:
        print(ls)
        if len(ls) > max_len:
            max_len = len(ls)
    return max_len        

    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # a = [4, 6, 5, 3, 3, 1]
    a = [1, 2, 2, 3,1, 2]
    # print(a)
    result = pickingNumbers(a)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
