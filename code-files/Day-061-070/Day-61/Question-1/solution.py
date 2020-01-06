import statistics
def sherlockAndStrings(s):
    dictOfString = {}
    modeList = []
    for eachCharachter in s:
        if eachCharachter not in dictOfString:
            dictOfString[eachCharachter] = 1
        else:
            dictOfString[eachCharachter] += 1
    for values in dictOfString.items():
        modeList.append(values[1])
    try:
        modeValue = statistics.mode(modeList)
    except:
        returnValue = "NO"
        #print("here")
        return returnValue
    #print(modeValue)
    returnValue = False
    counter = 1
    print(dictOfString)
    for values in dictOfString.items():
        if values[1] - modeValue == 1 and counter == 1:
            counter -= 1
            returnValue = True
        elif values[1] - modeValue >= 1 and counter == 0:
            returnValue = False
        #elif:
        else:
            #print("here")
            returnValue = True
            
    return returnValue
            
sherlockAndStrings("aabbccddeefghi")