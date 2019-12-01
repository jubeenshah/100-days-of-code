def capitalizeWord(string):
    listOfWord = string.split(' ')
    listToReturn = []
    for eachWord in listOfWord:
        if eachWord == '':
            listToReturn.append(eachWord)
            continue
        upperChar = eachWord[0].upper()
        eachWord = upperChar + eachWord[1:]
        listToReturn.append(eachWord)
        
    return ' '.join(listToReturn)

capitalizeWord("hello world testing      ")