def excelCollumnName(n:int)->str:
    dictOfChar = {i-65:chr(i) for i in range(65,91)}
    strToReturn = ""
    while n > 0:
        char = dictOfChar[(n-1)%26]
        n = (n-1) // 26
        print(n,char)
        strToReturn += char
        
    return strToReturn[::-1]

excelCollumnName(98765432123456789)