def isValid(s):
    leftBrackets = ['(', '[','{']
    rightBrackets = [')', ']','}']
    valid = {'{':'}', '(':')', '[':']'}
    if s == "":
        return True
    if len(s) %2 != 0:
        return False
    stack = []
    returnValue = False
    for each in s:
        if each in leftBrackets:
            stack.append(each)
        else:
            print(stack,each)
            if stack != []:
                checkParantheses = stack.pop()
                if valid[checkParantheses] == each:
                    returnValue = True
                    continue
                else:
                    return False
    
    if stack != []:
        return False
    return returnValue


isValid('[])')