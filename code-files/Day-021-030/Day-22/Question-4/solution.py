def hurdleRace(k, height):
    if k > max(height):
        return 0
    else:
        return max(height)-k

hurdleRace(1, [1, 6, 3, 5, 2])