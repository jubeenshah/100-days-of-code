def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    
    for a in arr:
        if a < 0:
            neg += 1
        elif a > 0:
            pos += 1
        else:
            zer += 1
    return (pos/len(arr), neg/len(arr), zer/len(arr))

plusMinus([-4, 3, -9, 0, 4, 1])