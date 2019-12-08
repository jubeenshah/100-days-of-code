#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    listToReturn = []
    listToReturn.append(len(arr))
    while arr:
        arr = sorted(arr,reverse=True)
        minimum = min(arr)
        #print(minimum)
        for i in range(len(arr)):
            arr[i] -= minimum
            #print(arr)
        try:
            while arr[-1] == 0:
                arr.pop()
        except:
            continue
        #print(arr)
        listToReturn.append(len(arr))
    return (listToReturn)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
