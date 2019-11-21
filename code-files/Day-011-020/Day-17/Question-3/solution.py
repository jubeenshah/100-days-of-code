def addBinary(a: str, b: str) -> str:
    counter = 0
    decRepA,decRepB = 0, 0 
    a = a[::-1]
    b = b[::-1]
    for i in a:
        print(decRepA,(int(i), (2 **counter)))
        decRepA = decRepA + (int(i) * (2 **counter))
        counter += 1
    print(decRepA)
    counter = 0
    for i in b:
        decRepB = decRepB + (int(i) * (2 **counter))
        counter += 1
    print(decRepB)
    print()
    print(decRepA+decRepB)
    return ('{:b}'.format(decRepA+decRepB))

addBinary("1010","1011")