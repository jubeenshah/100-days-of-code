def findDigits(n:int) -> int:
    stringOfNumber = str(n)
    #print(type(stringOfNumber),type(n))
    returnVal = 0
    for eachDigit in stringOfNumber:
        try:
            if n % int(eachDigit) == 0:
                returnVal += 1
        except:
            continue
    return returnVal
findDigits(12)