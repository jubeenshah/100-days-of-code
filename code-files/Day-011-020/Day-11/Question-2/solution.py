def longestPrefix2(m):
    if not m: return ''

    s1 = min(m)
    s2 = max(m)
    print(s1,s2)
    for i, c in enumerate(s1):
        print(s2[i],c,s1)
        if c != s2[i]:
            return s1[:i] #stop until hit the split index
    return s1

longestPrefix2(["abc","adbc","fec"])