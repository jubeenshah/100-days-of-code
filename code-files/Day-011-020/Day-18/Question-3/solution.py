dictFibo = {}
def climbingStairs(n):
    global dictFibo
    if n in dictFibo:
        ans = dictFibo[n]
    elif n < 2:
        ans = 1
        dictFibo[n] = ans
    else:
        ans = climbingStairs(n-1) + climbingStairs(n-2)
        dictFibo[n] = ans
    return ans
climbingStairs(2)