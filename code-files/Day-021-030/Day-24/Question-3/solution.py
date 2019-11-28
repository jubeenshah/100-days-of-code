def checkClassCancelled(k, a):
    a.sort()
    for i in range(k):
        if a[i] <= 0:
            continue
        else:
            return "Yes"
    return "No"

checkClassCancelled(int(input()),list(map(int, input().rstrip().split())))