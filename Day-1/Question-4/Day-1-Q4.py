# import collections
def repeatedString(s, n):
    a = s.count("a")
    length = len(s) 
    times = n // length * a
    remaining = n % length
    for i in s:
        if remaining == 0:
            break
        if i == "a":
            times += 1
        remaining -= 1
    print(times)
    return times
repeatedString("jdiacikk",899491)