def romanToInt(s) ->int:
    dictRomanToInt = {'I'    :         1,
                      'V'    :         5,
                      'X'    :         10,
                      'L'    :         50,
                      'C'    :         100,
                      'D'    :         500,
                      'M'    :         1000}
    intValueToReturn = 0
    s = s[::-1]
    for currentChar in range(1,len(s)):
        if s[currentChar].capitalize() in dictRomanToInt:
            #print(dictRomanToInt[currentChar])
            #print(dictRomanToInt[s[currentChar]],dictRomanToInt[s[currentChar-1]],currentChar)
            if dictRomanToInt[s[currentChar]] >= dictRomanToInt[s[currentChar-1]]:
                intValueToReturn += dictRomanToInt[s[currentChar]]
                #print(intValueToReturn,"+")
            else:
                intValueToReturn -= dictRomanToInt[s[currentChar]]
                #print(intValueToReturn,"-")
    intValueToReturn += dictRomanToInt[s[0]]
    #print(intValueToReturn)
    return intValueToReturn
romanToInt("VCIICD")