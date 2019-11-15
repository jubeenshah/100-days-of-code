def binaryCount(n):
    binary = '{:064b}'.format(n)
    print(binary)
    count = 0
    maxCount = float('-inf')
    for bit in binary:
        if bit == '1':
            count+=1
            if count > maxCount:
                maxCount = count
        else:
            count = 0
    return maxCount
for i in range(1,20):
    print(binaryCount(i))