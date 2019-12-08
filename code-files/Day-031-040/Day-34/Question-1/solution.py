def libraryFine(rd, rm, ry, ed, em, ey):
    if (ry, rm, rd) <= (ey, em, ed):
        return (0)
    elif (ry, rm) == (ey, em):
        return (15 * (rd - ed))
    elif ry == ey:
        return (500 * (rm - em))
    else:
        return (10000)

            
libraryFine(28,2,2015,15,4,2015)