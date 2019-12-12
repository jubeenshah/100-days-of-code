def titleToNumber(s: str) -> int:
    returnValue = 0
    for char in s:
        returnValue = returnValue * 26 + ord(char)-ord('A')+1
    return returnValue
    

titleToNumber("BBACAC")