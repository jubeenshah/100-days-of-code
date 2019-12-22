import math
def encryption(s)->str:
    s = ''.join(s.strip(" ").split(" "))
    lengthOfS = math.sqrt(len(s))
    numRows = math.floor(lengthOfS)
    numCols = math.ceil(lengthOfS)
    #print(s,lengthOfS,numRows,numCols)
    start = 0
    end = numCols
    encryptList = []
    for i in range(numRows):
        encryptList.append(s[start:end])
        start = end
        end = end + numCols
    print(encryptList)
    returnString = ""
    counter = 0
    i = 0
    while counter < len(encryptList):
        if i == len(encryptList):
            #print("in")
            i = 0
            counter += 1
        #print(encryptList[i][counter])
        #print(i,len(encryptList))
        try:
            returnString+= encryptList[i][counter]
        except:
            break
        #print("lolu")
        i+=1

    print(returnString)
        
            

encryption("if man was meant to stay on the ground god would have given us roots")