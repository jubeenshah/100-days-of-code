def countingValleys(n, s):
    valueToReturn = 0
    array = []
    for i in s:
        
        if i == "U":
            valueToReturn += 1
        if i == "D":
            valueToReturn -= 1
        array.append(valueToReturn)
        #print(valueToReturn)
    numberOfValleys = 0    
    for i in range(len(array)):
        if array[i] == 0 and array[i-1]<0:
            numberOfValleys += 1
    print(numberOfValleys)
    return numberOfValleys

x = countingValleys(10,"UDDDUDUDUU")
print(x)