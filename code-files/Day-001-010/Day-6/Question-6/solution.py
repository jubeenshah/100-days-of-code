def flippingBits(n):
    binary = '{:032b}'.format(n)
    newBinary = ''
    for bit in binary:
        if bit == '1': 
            newBinary += '0' 
        else: 
            newBinary += '1'
    return int(newBinary,2)
flippingBits(0)