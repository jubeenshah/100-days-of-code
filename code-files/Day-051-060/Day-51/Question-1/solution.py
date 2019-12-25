# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())


def calculateMBC(ab,bc):
    return str(round(math.degrees(math.atan2(ab,bc))))+"°"
    

print(calculateMBC(ab,bc))
#calculateMBC(ab,bc)

