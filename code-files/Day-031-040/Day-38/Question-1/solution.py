from itertools import combinations

def mergeLists(listOne,listTwo): 
    newList = [0]*len(listOne)
    for i in range(len(listOne)):
        if listOne[i] == 1 or listTwo[i] == 1:
            newList[i] = 1
        else:
            continue
    #print(newList)
    return sum(newList)

def acmTeam(topic):
    numberOfParticipants = len(topic)
    knowledgeDict = {topic.index(currentTopic):[int(x) for x in currentTopic] for currentTopic in topic}
    topicList = [[int(x) for x in eachTopic] for eachTopic in topic]
    #print(topicList)
    topicCombination = list(combinations(topicList,2))
    maxKnowledge = float('-inf')
    numberOfTeamsWithMaxKnowledge = 0
    listOfScores = []
    for each in topicCombination:
        currentScore = mergeLists(each[0],each[1])
        #print(currentScore,each[0],each[1])
        if currentScore > maxKnowledge:
            maxKnowledge = currentScore
        listOfScores.append(currentScore)
        #if currentScore == maxKnowledge:
            #numberOfTeamsWithMaxKnowledge += 1
    for score in listOfScores:
        if score == maxKnowledge:
            numberOfTeamsWithMaxKnowledge += 1
    return [maxKnowledge,numberOfTeamsWithMaxKnowledge]
    




acmTeam(['10101', '11100', '11010', '00101'])

