def coolguy(arr):
    ans = 0
    n = len(arr)
    for a in range(1,n+1):
        print("A",a)
        for b in range(a,n+1):
            print("B",b)
            for c in range(b+1,n+1):
                print("C",c)
                for d in range(c,n+1):
                    print("D",d)
                    ans = ans + min(functionF(arr,a,b), functionF(arr,c,d))
                    print(a,b,c,d,ans)
    return ans % (10**9 +7)
def functionF(arr,a,b):
    minimumValue = float('inf')
    for i in range(a-1,b):
        minimumValue = min(minimumValue,arr[i])
    return minimumValue

functionF([3,2,1],1,2)

coolguy(arr)