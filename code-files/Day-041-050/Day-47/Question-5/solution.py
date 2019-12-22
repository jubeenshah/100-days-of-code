def reverseBits(n) -> int:
    oribin='{0:032b}'.format(n)
    reversebin=oribin[::-1]
    return int(reversebin,2)

reverseBits(43261596)