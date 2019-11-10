def countApplesAndOranges(s, t, a, b, apples, oranges):
    startHouse = s
    endHouse = t
    appleTree = a
    orrageTree = b
    listOfAppleDistance = apples
    listOfOrangeDistance = oranges
    numberOfApples = 0
    numberOfOranges = 0

    for apple in listOfAppleDistance:
        #apple tree is on the left
        print(apple + appleTree)
        if (apple + appleTree) >= startHouse and (appleTree + apple) <= endHouse:
            numberOfApples += 1
        pass
    for orange in listOfOrangeDistance:
        #apple tree is on the left
        print(orange+orrageTree)
        if (orange + orrageTree) >= startHouse and (orange + orrageTree) <= endHouse:
            numberOfOranges += 1
        pass
    return numberOfApples, numberOfOranges 
    pass

print(countApplesAndOranges(7,11,5,15, [-2,2,1], [5,-6]))