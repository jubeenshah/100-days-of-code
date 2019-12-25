def printPallindrome(n):
    for i in range(1,n+1):
        stringToPrint = ""
        for j in range(1,i+1):
            stringToPrint += str(j)
        for k in range(i-1,0,-1):
            stringToPrint += str(k)
        print(stringToPrint)

printPallindrome(int(input()))