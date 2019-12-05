def jumpingOnClouds(arrayOfClouds:list,jumpValue:int,) -> int:
    #print(jumpValue,arrayOfClouds)
    startEnergy = 100
    stopRunning = False
    if jumpValue == len(arrayOfClouds):
        startPoint = 0
    else:
        startPoint = jumpValue
    while stopRunning != True:
        if (arrayOfClouds[startPoint]) == 1:
            startEnergy -= 2
        startEnergy -= 1
        if startPoint == 0:
            break
        #print(arrayOfClouds[startPoint],startEnergy)
        startPoint += jumpValue
        if startPoint >= len(arrayOfClouds):
            startPoint = startPoint % len(arrayOfClouds)
        else:
            pass
    return (startEnergy)

jumpingOnClouds(arrayOfClouds,19)