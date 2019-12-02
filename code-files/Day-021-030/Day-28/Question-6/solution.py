import math
def divide(dividend, divisor):
    #print(dividend,divisor)
    counter = 0
    temp = dividend
    while dividend >= 0:
        if divisor > 0:
            if dividend - divisor >= 0:
                dividend -= divisor
                #print(dividend)
                counter += 1
            else:
                break
        else:
            if dividend + divisor >= 0:
                dividend += divisor
                #print(dividend)
                counter -= 1
            else:
                break
    print(counter)
    return (math.ceil(temp / divisor)) == counter
divide(123123,123)    