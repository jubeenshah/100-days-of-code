def dayOfProgrammer(year):
    if year >= 1919:
        if (year % 400 == 0) or ((year % 4 ==0) and (year % 100 !=0)):
            returnString = '12.09.'+str(year)
        else:
            returnString ='13.09.'+str(year)
    elif year < 1918:
        if (year % 4 ==0):
            returnString ='12.09.'+str(year)
        else:
            returnString ='13.09.'+str(year)
    return returnString
dayOfProgrammer(2017)