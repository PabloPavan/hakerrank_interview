#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getShiftedString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER leftShifts
#  3. INTEGER rightShifts
#
from collections import deque

def getShiftedString(s, leftShifts, rightShifts):
    # Write your code here  

    fila_dupla = deque()

    for letra in s:
        fila_dupla.append(letra)

    fila_dupla.rotate(-leftShifts)
    fila_dupla.rotate(rightShifts)
        
    return "".join(fila_dupla)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    leftShifts = int(input().strip())

    rightShifts = int(input().strip())

    result = getShiftedString(s, leftShifts, rightShifts)

    fptr.write(result + '\n')

    fptr.close()
