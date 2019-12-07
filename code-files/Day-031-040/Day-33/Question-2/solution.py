import math
def squares(a, b):
    counter = 0
    start = int(math.sqrt(a))
    end = int(math.sqrt(b))
    for i in range(start,end+1):
        if i**2 >= a and i**2 <= b:
            counter += 1
    return counter

squares(465868129, 988379794)