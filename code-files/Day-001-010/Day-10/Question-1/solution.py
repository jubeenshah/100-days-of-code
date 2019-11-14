import random
lenA = random.randint(1,10**5)
lenB = random.randint(1,10**5)
lenC = random.randint(1,10**5)
randomListA = [random.randint(1,10**8) for _ in range(1,lenA)]
randomListB = [random.randint(1,10**8) for _ in range(1,lenB)]
randomListC = [random.randint(1,10**8) for _ in range(1,lenC)]
#print(len(randomListA), len(randomListB), len(randomListC))
def triplets(a, b, c):
    a, b, c = map(lambda x: sorted(set(x)), (a, b, c))
    i_p = 0
    i_r = 0
    count = 0
    for q in b:
        while i_p < len(a) and a[i_p] <= q:
            i_p += 1
            
        while i_r < len(c) and c[i_r] <= q:
            i_r += 1
        
        count += i_p * i_r
    return count
               

triplets(randomListA,randomListB,randomListC)