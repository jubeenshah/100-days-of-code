def appendAndDelete(s, t, k):
    start = 0
    if s == t and k>=len(s):
        return 'Yes'
    else:
        for i,j in zip(s,t):
            if i == j:
                start += 1
                continue
            else:
                break
        if (len(t[start:]) == 0):
            if len(s) + len(t) <= k:
                return 'Yes'
            else:
                return 'No'
        else:
            if (len(s[start:])+len(t[start:]) <= k):
                return "Yes"
            else:
                return "No"

appendAndDelete("zzzzz","zzzzzzz",4)