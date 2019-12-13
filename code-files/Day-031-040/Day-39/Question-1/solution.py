def average(array):
    # your code goes here
    average = 0
    if not array:
        return average
    
    setArray = set(array)
    sumOfDistinctsHeights = sum(setArray)
    totalNumDistinHeights = len(setArray)
    average = sumOfDistinctsHeights / totalNumDistinHeights
    return average
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)