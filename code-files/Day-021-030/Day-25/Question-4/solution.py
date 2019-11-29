#!/bin/python3

import math
import os
import random
import re
import sys

def getReverse(number):
    tempStr = str(number)
    tempStr = (tempStr[::-1])
    return int(tempStr)

# Complete the beautifulDays function below.
def beautifulDay(start,end,k):
    numberOfBeautifulDays = 0
    for i in range(start,end+1):
        x = getReverse(i)
        if abs(x-i) % k == 0:
            numberOfBeautifulDays += 1
    return numberOfBeautifulDays

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDay(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
