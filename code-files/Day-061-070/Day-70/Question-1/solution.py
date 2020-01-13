def chocolateFeast(n, c, m):
    choc, wrappers = [int(n/c), int(n/c)]
    while (wrappers >= m):
        choc+= 1
        wrappers -= m
        wrappers += 1
    print(choc)
chocolateFeast(6,2,2)