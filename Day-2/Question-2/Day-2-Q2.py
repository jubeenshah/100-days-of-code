def leftRotate(arr,d):
    leftPart = arr[:d]
    rightpart = arr[d:]
    return rightpart +leftPart

print(leftRotate([1,2,3,4,5], 4))