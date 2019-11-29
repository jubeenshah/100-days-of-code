def stringFormatting(n:int):
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
        print('{:{width}d} {:{width}o} {:{width}X} {:{width}b}'.format(i,i,i,i,width=width))
    

stringFormatting(20)