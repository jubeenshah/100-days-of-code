def tryExcept(a,b):
    try:        
        print(int(a)//int(b))
    except ZeroDivisionError as err:
        print("Error Code:",err)
    except ValueError as err:
        print("Error Code:",err)
timesToRepeat = int(input())
for _ in range(timesToRepeat):
    a,b = input().split(" ")
    tryExcept(a,b)

