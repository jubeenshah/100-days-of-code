def lengthOfLastWord(s:str)->int:
    s = s.split(' ')
    #print(s,len(s[-1]))
    returnLen = 0
    for i in range(len(s)-1,-1,-1):
        #print(s[i],i)
        if s[i] != '':
            return len(s[i])
    return returnLen
lengthOfLastWord("   123 ")