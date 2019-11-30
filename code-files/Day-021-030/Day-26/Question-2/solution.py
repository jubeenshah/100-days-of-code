def viralAdvertisement(n:int)->int:
    dayNumber = 1
    shared = 5
    totalLiked = 0
    #print(dayNumber, shared, shared//2, totalLiked)
    while dayNumber != n+1:
        currentLiked = shared // 2
        totalLiked += currentLiked
        shared = currentLiked * 3
        #print(dayNumber, shared, currentLiked, totalLiked)
        dayNumber += 1
    return totalLiked   

viralAdvertisement(5)