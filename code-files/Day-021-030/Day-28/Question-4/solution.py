# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
def printPermutations(string,k):
    string = string.upper()
    listOfPermutations = list(permutations(string,k))
    listOfPermutations.sort()
    for eachSubstring in listOfPermutations:
        print(''.join(eachSubstring))

string, k = map(str, input().split(' '))
printPermutations(string,int(k))