def fizzbuzz(n):
    lisToReturn = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 != 0:
            lisToReturn.append("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            lisToReturn.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            lisToReturn.append("FizzBuzz")
        else:
            lisToReturn.append(str(i))
    return lisToReturn

fizzbuzz(15000)