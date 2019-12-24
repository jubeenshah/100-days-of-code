def matchingStrings(strings, queries):
    dictOfResponses = {}
    responseList = []
    for eachString in strings:
        if eachString not in dictOfResponses:
            dictOfResponses[eachString] = 1
        elif eachString in dictOfResponses:
            dictOfResponses[eachString] += 1
    for eachQuery in queries:
        if eachQuery in dictOfResponses:
            responseList.append(dictOfResponses[eachQuery])
        else:
            responseList.append(0)
    return responseList
            

matchingStrings(['ab','ab','abc'],['ab','abc','bc'])