def taumBday(b, w, bc, wc, z):
    if bc == wc:
        return ((b*bc)+w*wc)
    elif bc > wc + z:
        #print("BC")
        return ((w*wc)+(b*(wc+z)))
    elif wc > bc + z:
        #print("WC")
        return ((b*bc)+(w*(bc+z)))
    else:
        #print("here")
        return ((b*bc)+w*wc)

taumBday(10,10,1,1,1)