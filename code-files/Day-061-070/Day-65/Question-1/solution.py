# Enter your code here. Read input from STDIN. Print output to STDOUT

numElementsSetA = int(input())
setA = set(map(int, input().split(" ")))
numElementsSetB = int(input())
setB = set(map(int, input().split(" ")))

def printSortedSymmetricDifference(setA, setB):
    diffA = list(setA.difference(setB))
    diffB = list(setB.difference(setA))
    diffToReturn = []
    diffToReturn.extend(diffA)
    #print(diffToReturn)
    diffToReturn.extend(diffB)
    #print(diffToReturn)
    diffToReturn.sort()
    for each in diffToReturn:
        print(each)



printSortedSymmetricDifference(setA,setB)