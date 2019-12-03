N = int(input())
listOfFirstName = []
listOfEmailAddress = []
for N_itr in range(N):
    firstNameEmailID = input().split()

    firstName = firstNameEmailID[0]
    listOfFirstName.append(firstName)
    emailID = firstNameEmailID[1]
    listOfEmailAddress.append(emailID)

import re
def findGmail(firstName, emailAddress):
    #print(firstName, emailAddress)
    listToReturn = []
    for firstNameVal, emailVal in zip(firstName,emailAddress):
        x = (re.findall(pattern="@gmail.com", string=emailVal))
        if  x == ["@gmail.com"]:
            #print(firstNameVal,emailVal)
            listToReturn.append(firstNameVal)
    listToReturn.sort()
    print('\n'.join(listToReturn))
findGmail(listOfFirstName, listOfEmailAddress)