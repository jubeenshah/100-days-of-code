from collections import OrderedDict
def wordorder(wordlist):
    returnOrderedDict = OrderedDict()
    returnList = []
    for word in wordlist:
        if word not in returnOrderedDict:
            returnOrderedDict[word] = 1
        else:
            returnOrderedDict[word] += 1
    for items in returnOrderedDict.items():
        returnList.append(str(items[1]))
    return returnList

#wordlist = ['bcdef', 'abcdefg', 'bcde','bcdef']
numWords = int(input())
wordlist = []
for _ in range(numWords):
    wordInput = input()
    wordlist.append(wordInput)

printReturnList = wordorder(wordlist)
print(len(printReturnList))
print(' '.join(printReturnList))