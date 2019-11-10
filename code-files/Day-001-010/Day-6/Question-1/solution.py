def countSwaps(a):
    counter = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                #print(a[i],a[j])
                a[j], a[j+1] = a[j+1], a[j]
                counter += 1
        print(a)
    print("Array is sorted in ",counter ,"swaps.")
    print("First Element: ", a[0])
    print("Last Element: ", a[len(a)-1])
    pass

countSwaps([6,2,1])