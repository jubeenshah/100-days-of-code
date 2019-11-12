def reverse(x):
    if x < 0:
        isNegative = True
    else:
        isNegative = False
    listX= [char for char in str(abs(x))]
    listX.reverse()
    listX = (''.join(listX))
    if isNegative:
        listX = -1 * int(listX)
    if int(listX) > 2**31 or int(listX) < -2**31:
        return 0
    return (int(listX))
reverse(1534236469)