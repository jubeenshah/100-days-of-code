def arrayRotation(a, k , queries):
    numberOfRotaions = k
    array = a
    numberOfTimesToRunLoop = k % len(array)
    array = array[-numberOfTimesToRunLoop:] + array[:len(array)-numberOfTimesToRunLoop]
    for eachQuery in queries:
        print(array[eachQuery])
arrayRotation([1,2,3], 2, [0,1,2])