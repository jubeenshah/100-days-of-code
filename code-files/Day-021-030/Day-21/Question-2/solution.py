def longestPalindrome(s: str) -> str:
    maxLen = float('-inf')
    maxLenDict = {}
    for i in range(len(s)-1,0,-1):
        for j in range(len(s)-1,0,-1):
            #print(s[i:j+1])
            if s[i:j+1] == "" or len(s[i:j+1])<maxLen:
                continue
            if isPallindrome(s[i:j+1]):
                if len(s[i:j+1]) > maxLen:
                    maxLen = len(s[i:j+1])
                    maxLenDict[maxLen] = s[i:j+1]
                if len(s[i:j+1]) == len(s):
                    return s[i:j+1]
    print(maxLenDict)
    return (sorted(maxLenDict.items(), key=lambda lv:lv[0],reverse=True)[0][1])

def isPallindrome(substring:str) ->bool:
    temp = ""
    for s in substring[::-1]:
        temp+=s
    return (temp==substring)
isPallindrome(a)

longestPalindrome(a)