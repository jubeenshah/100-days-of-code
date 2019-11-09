import collections
def checkMagazine(magazine, note):
    printVal = "0"
    if len(note) > len(magazine):
            printVal = "No"
    magazineCollection = dict(collections.Counter(magazine.split(" ")))
    for value in note.split(" "):
        if value in magazineCollection and magazineCollection[value] != 0:
            magazineCollection[value] -= 1
            #print(value,magazineCollection[value])
            continue
        else:
            #print("here")
            printVal = "No"
    if printVal == "No":
        print("No")
    else:
        print("Yes")

checkMagazine("o l x imjaw bee khmla v o v o imjaw l khmla imjaw x","imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o")