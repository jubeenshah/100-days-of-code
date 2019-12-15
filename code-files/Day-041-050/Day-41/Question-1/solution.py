# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict
n,m = map(int, (input().split(" ")))

firstList = [(input()) for _ in range(n)]
secondList = [(input()) for _ in range(m)]

defaultDict = defaultdict(list)
index = 1
for eachWord in firstList:
    defaultDict[eachWord].append(str(index))
    index += 1
#print(defaultDict)
for eachWord in secondList:
    if len(defaultDict[eachWord])>0:
        print(' '.join((defaultDict[eachWord])))
    else:
        print('-1')