#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p,q):
    if p <= 1:
        returnList = [1]
    else:
        returnList = []
    for num in range(p,q+1):
        if isKaprekar(num):
            returnList.append(num)
        else:
            continue
    #return returnList
    if returnList:
        for each in returnList:
            print(each, end=" ")
    else:
        print("INVALID RANGE")

def isKaprekar(num):
    square = str(num ** 2)
    #print(square)
    firstHalf = square[:len(square)//2]
    secondHalf = square[len(square)//2:]
    #print(firstHalf,secondHalf)
    try:
        if int(firstHalf) + int(secondHalf) == num:
            return True
        else:
            return False
    except:
        return False


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
