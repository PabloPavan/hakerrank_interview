#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countDuplicate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def countDuplicate(numbers):
    # Write your code here
    dic_number = {}
    count = 0
    for i in numbers:
        if i not in dic_number:
            dic_number[i] = 1
        else:
            dic_number[i] += 1
    for valor in dic_number.values():
        if valor > 1:
            count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = countDuplicate(numbers)

    fptr.write(str(result) + '\n')

    fptr.close()
