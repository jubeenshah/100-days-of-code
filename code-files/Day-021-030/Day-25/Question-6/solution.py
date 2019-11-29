def intToRoman(num):
    intToRomanDict={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
    answerToReturn=''
    if num in intToRomanDict:
        return intToRomanDict[num]
    else:
        for k,v in intToRomanDict.items():
            while(num-k>=0):
                num=num-k
                answerToReturn+=v
            if(num==0):
                break
        return answerToReturn

intToRoman(8)