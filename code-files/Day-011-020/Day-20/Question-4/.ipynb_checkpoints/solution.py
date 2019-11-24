def lengthOfLongestSubstring(s):
    maxLength = float('-inf')
    if not s:
        return 0
    listOfSubstrings = []
    for i in range(len(s)):
        tempList = []
        for j in s[i:]:
            if j in tempList:
                break
            else:
                tempList.append(j)
        if len(tempList) > maxLength:
            maxLength = len(tempList)
    print(maxLength)
    pass

lengthOfLongestSubstring("abcabcbb")