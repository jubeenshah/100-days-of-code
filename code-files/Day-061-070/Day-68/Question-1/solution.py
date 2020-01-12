def beautifulTriplets(d,num):
    numberToReturn = 0
    for i in range(len(num)):
        if num[i] + d in num and num[i]+2*d in num:
            numberToReturn += 1
    return numberToReturn

beautifulTriplets(5,list(map(int, input().split(" "))))