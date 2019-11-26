#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(sizeArray, string):
    dictOfSize = {}
    index = 0
    for i in range(97,123):
        dictOfSize[chr(i)] = sizeArray[index]
        index += 1
    #print(dictOfSize)
    
    maxheight = float('-inf')
    for char in string:
        if char in dictOfSize:
            if dictOfSize[char] > maxheight:
                maxheight = dictOfSize[char]
                
    return (maxheight*len(string))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
