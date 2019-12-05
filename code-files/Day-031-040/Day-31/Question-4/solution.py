import itertools
def isValidParantheses(stringParantheses) -> bool:
    queue = []
    for eachParantheses in stringParantheses:
        if eachParantheses == '(':
            queue.append(eachParantheses)
        else:
            try:
                test = queue.pop()
            except:
                return False
    if queue == []:
        return True
    
isValidParantheses("((()))")

def generateParantheses(n):
    paranthesesList = []
    for i in range(n):
        paranthesesList.append('(')
        paranthesesList.append(')')
    permutationOfParantheses = list(itertools.permutations(paranthesesList))
    listToReturn = []
    for eachPermutation in permutationOfParantheses:
        stringToPass = ''.join(eachPermutation)
        #print(stringToPass)
        checkValidity = isValidParantheses(stringToPass)
        print(stringToPass, checkValidity)
        if stringToPass[0] == ')':
            continue
        if checkValidity:
            if stringToPass in listToReturn:
                continue
            else:
                listToReturn.append(stringToPass)
    print(listToReturn)

generateParantheses(5)