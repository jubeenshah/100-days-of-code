#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    seq = [[]]*n
    #print(seq)
    returnList = []
    for eachQuery in queries:
        #print(eachQuery)
        
        seqIndex = 0
        if eachQuery[0] == 1:
            seqIndex = (eachQuery[1]^lastAnswer)%n
            if len(seq[seqIndex]) == 0:
                seq[seqIndex] = [eachQuery[2]]
            else:
                seq[seqIndex].append(eachQuery[2])
            #print(seq[seqIndex])
        elif eachQuery[0] == 2:
            seqIndex = (eachQuery[1]^lastAnswer)%n
            lastAnswer = seq[seqIndex][eachQuery[2]%len(seq[seqIndex])]
            print(lastAnswer)
            returnList.append(lastAnswer)
        #print(seq)
        #print()
    #print(seq)
    #return lastAnswer
    return returnList

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
