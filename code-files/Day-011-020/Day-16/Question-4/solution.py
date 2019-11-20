def plusOne(digits: list) -> list:
    if len(digits) == 0:
        digits.append(1)
        return digits
        
    digits.reverse()
    carry = 0
    for d in range(len(digits)):
        temp = carry + digits[d] + 1 if d == 0 else carry + digits[d]
        if temp >= 10:
            temp, carry = temp%10, 1
        else:
            temp, carry = temp, 0
        digits[d] = temp

    if carry:
        digits.append(carry)
    digits.reverse()
    return digits

testList = []
for i in range(10):
    for j in range(10):
        testList.append([i,j])
#print(testList)
    
for i in testList:
    print(i,end="-->")
    print(plusOne(i))
    