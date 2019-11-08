def staircase(n):
    count = 1
    while n >0:
        space = " "* (n-1)
        hashtag = "#"*count
        print(space+hashtag)
        n -= 1
        count+=1

print(staircase(19))