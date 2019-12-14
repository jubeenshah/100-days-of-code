def sortUsingQS(A):
    print(A)
    a = quicksort(A,0,len(A)-1)
    return a
    
def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
    return A
        
        
def partition(A,p,r):
    x = A[r]
    i = p-1
    print(A)
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1],A[r] = A[r], A[i+1]
    return i+1
array = [random.randint(1,100) for x in range(100)]
sortUsingQS(array)