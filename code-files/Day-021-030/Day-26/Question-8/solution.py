def phoneLetterCombination(digits):
    if not digits:
        return []
    dictOfPhoneToLetters = {'2': ["a","b","c"],
                            '3': ["d","e","f"],
                            '4': ["g","h","i"],
                            '5': ["j","k","l"],
                            '6': ["m","n","o"],
                            '7': ["p","q","r","s"],
                            '8': ["t","u","v"],
                            '9': ["w","x","y","z"]}
    listToReturn = ['']
    for d in digits:
        temp = []
        for b in dictOfPhoneToLetters[d]:
            for a in listToReturn:
                #print(listToReturn,temp)
                temp.append(a+b)
        listToReturn = temp.copy()
    return listToReturn
phoneLetterCombination("34567897643")