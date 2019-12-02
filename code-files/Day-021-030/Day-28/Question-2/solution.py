def removeDuplicates(string):
    stringToReturn = ""
    counter = 0
    for i in range(0,len(string)):
        if string[i] in stringToReturn and counter > 0:
            continue
        else:
            #print(stringToReturn)
            stringToReturn += string[i]
            counter+=1
    return (stringToReturn)

removeDuplicates("ADADADSASDASD")
def mergeTheTools(string, k):
    listOfKseperatedStrings = [string[i:i+k] for i in range(0,len(string),k)]
    for eachSubstring in listOfKseperatedStrings:
        #print(eachSubstring)
        stringToPrint = removeDuplicates(eachSubstring)
        print(stringToPrint)

mergeTheTools("AABCAAADA",3)