def calcScore(string, listOfVowels):
    stuartScore = 0
    kevinScore = 0
    #print(string,listOfVowels)
    for i in range(len(string)):
        if string[i] in listOfVowels:
            print(kevinScore)
            kevinScore += (len(string)-i)
        else:
            print(stuartScore)
            stuartScore += (len(string)-i)
    return stuartScore,kevinScore

def theMinionGame(string):
    listOfVowels = ['A','E','I','O','U']
    stuartScore,kevinScore = calcScore(string, listOfVowels)
    if stuartScore > kevinScore:
        print("Stuart", stuartScore)
    elif stuartScore < kevinScore:
        print("Kevin",kevinScore)
    else:
        print("Draw")

theMinionGame("BANANANAAAS")