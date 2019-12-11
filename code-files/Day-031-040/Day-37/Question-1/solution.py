def generateBoard(length, obstacles,rowQueen, collumnQueen)->list:
    boardMatrix = [[0 for x in range(length)] for x in range(length)]
    #boardMatrix = [[random.randint(1,120) for x in range(5)] for x in range(5)]
    #for each in boardMatrix:
    #    print(each)
    #print()
    for element in obstacles:
        #print(boardMatrix[element[0]-1][element[1]-1])
        boardMatrix[element[0]-1][element[1]-1] = -1
    #print()
    #for each in boardMatrix:
    #    print(each)
    boardMatrix[rowQueen-1][collumnQueen-1] = 1
    return boardMatrix
#generateBoard(5,[[5,5],[1,1],[2,5]])

def queensAttack(lengthOfSides, numberOfObstacles, rowQueen, collumnQueen, obstaclesArray):
    if not lengthOfSides:
        return 0
    generatedChessBoard = generateBoard(lengthOfSides,obstaclesArray,rowQueen, collumnQueen)
    #generatedChessBoard = [[random.randint(1,9) for x in range(5)] for x in range(5)]
    for each in generatedChessBoard:
        print(each)
    numberOfAttacks = 0
    
    print("Moving-Up")
    startRow, startCol = rowQueen-1, collumnQueen
    while(startRow > 0):
        print(generatedChessBoard[startRow-1][startCol-1])
        if (generatedChessBoard[startRow-1][startCol-1]) == 0:
            numberOfAttacks += 1
        else:
            break
            #pass
        startRow -= 1
    print(numberOfAttacks)
    print("Moving-Down")
    startRow, startCol = rowQueen+1, collumnQueen
    while(startRow <= len(generatedChessBoard)):
        print(generatedChessBoard[startRow-1][startCol-1])
        if (generatedChessBoard[startRow-1][startCol-1]) == 0:
            numberOfAttacks += 1
        else:
            break
            #pass
        startRow += 1
    print(numberOfAttacks)
    
    print("Moving-Up-diag-right")
    startRow, startCol = rowQueen-1, collumnQueen+1
    while(startRow >= 0 and startCol <=len(generatedChessBoard)):
        print(generatedChessBoard[startRow-1][startCol-1])
        if (generatedChessBoard[startRow-1][startCol-1]) == 0:
            numberOfAttacks += 1
        elif (generatedChessBoard[startRow-1][startCol-1]) == 1:
            startRow -= 1
            startCol += 1
            pass
        else:
            break
            #pass
        startRow -= 1
        startCol += 1
    print(numberOfAttacks)
    
    print("Moving-Up-diag-left")
    startRow, startCol = rowQueen-1, collumnQueen-1
    while(startRow > 0 and startCol >0):
        print(generatedChessBoard[startRow-1][startCol-1])
        if (generatedChessBoard[startRow-1][startCol-1]) == 0:
            numberOfAttacks += 1
        else:
            break
            #pass
        startRow -= 1
        startCol -= 1
    print(numberOfAttacks)
    
    print("Moving-down-diag-left")
    startRow, startCol = rowQueen+1, collumnQueen-1
    while(startRow <= len(generatedChessBoard) and startCol > 0):
        print(generatedChessBoard[startRow-1][startCol-1])
        if (generatedChessBoard[startRow-1][startCol-1]) == 0:
            numberOfAttacks += 1
        else:
            break
            #pass
        startRow += 1
        startCol -= 1
    print(numberOfAttacks)
    
    print("Moving-down-diag-right")
    startRow, startCol = rowQueen+1, collumnQueen+1
    while(startRow <= len(generatedChessBoard) and startCol <= len(generatedChessBoard)):
        print(generatedChessBoard[startRow-1][startCol-1])
        if (generatedChessBoard[startRow-1][startCol-1]) == 0:
            numberOfAttacks += 1
        elif (generatedChessBoard[startRow-1][startCol-1]) == 1:
            startRow += 1
            startCol += 1
            pass
        else:
            break
            #pass
        startRow += 1
        startCol += 1
    print(numberOfAttacks)
    
    print("Moving-left")
    startRow, startCol = rowQueen, collumnQueen-1
    while(startRow <= len(generatedChessBoard) and startCol > 0):
        print(generatedChessBoard[startRow-1][startCol-1])
        if (generatedChessBoard[startRow-1][startCol-1]) == 0:
            numberOfAttacks += 1
        else:
            break
            #pass
        startCol -= 1
    print(numberOfAttacks)
    
    print("Moving-right")
    startRow, startCol = rowQueen, collumnQueen+1
    while(startRow <= len(generatedChessBoard) and startCol <= len(generatedChessBoard)):
        print(generatedChessBoard[startRow-1][startCol-1])
        if (generatedChessBoard[startRow-1][startCol-1]) == 0:
            numberOfAttacks += 1
        else:
            break
            #pass
        startCol += 1
    print(numberOfAttacks)
    return numberOfAttacks
#queensAttack(5,3,4,3,[[5,5],[4,2],[2,3]])
#queensAttack(4,0,4,4,[])
#queensAttack(lengthOfSides=0, numberOfObstacles=0, rowQueen=1, collumnQueen=1, obstaclesArray=[])
queensAttack(lengthOfSides=5, numberOfObstacles=1, rowQueen=4, collumnQueen=4, obstaclesArray=[[3,5]])