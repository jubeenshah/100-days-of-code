n, m = map(int, input().split(" "))
array = list(map(int, input().split(" ")))
A = set(map(int, input().split(" ")))
B = set(map(int, input().split(" ")))
import collections
def calculateHappiness(array, A, B):
    score = 0
    arrayCounter = collections.Counter(array)
    print(arrayCounter)
    for eachElement in array:
        if eachElement in A:
            score += 1
        elif eachElement in B:
            score -= 1
        else:
            continue
    return score

calculateHappiness(array, A, B)