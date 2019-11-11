def makeAnagram(a, b):
    count = 0
    for i in range(97, 123):
        ia = a.count(chr(i))
        print(chr(i),"count in a:",ia, end="")
        ib = b.count(chr(i))
        print("|", chr(i),"count in b:",ib, end="")
        count += abs(ia-ib)
        print("| Difference = ", abs(ia-ib))
        print()
    return count
makeAnagram("abcc", "abc")