def kangaroo(x1, v1, x2, v2):
    counter = 0
    if x2 > x1 and ((v2 > v1) or (v2 == v1)):
        return ("NO")
    while x1!=x2:
        x1 += v1
        x2 += v2
        counter += 1
        if x1 > x2:
            return "NO"
        #print(x1,x2, counter)
    return "YES"   

kangaroo(1, 2, 5, 2)