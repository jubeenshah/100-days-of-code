def breakingRecords(scores):
    numMinBroken = 0
    numMaxBroken = 0
    currentMin,currentMax = scores[0], scores[0]
    for score in scores:
        if score < currentMin:
            currentMin = score
            numMinBroken += 1
        if score >currentMax:
            currentMax = score
            numMaxBroken += 1
    return (numMaxBroken,numMinBroken)

breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])