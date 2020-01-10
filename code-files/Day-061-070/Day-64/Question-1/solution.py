def organizingContainers(container):
    #print(container)
    mr = []
    mc = []
    n = len(container)
    for i in range(n):
        mr.append(sum(container[i]))
        j = tot = 0
        for j in range(n):
            tot += container[j][i]
        mc.append(tot)
    mr.sort()
    mc.sort()
    if mr == mc:
        return "Possible"
    else:
        return "Impossible"
organizingContainers([[1, 3, 1], [2, 1, 2], [3, 3, 3]])