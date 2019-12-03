def isPallindrome(string)->bool:
    if string == "":
        return True
    string = string.lower()
    newString = ""
    for letters in string:
        if letters.isalnum():
            newString += letters
    print(newString)        
    return (newString==newString[::-1])

isPallindrome("9;8'4P?X:1Q8`dOfJuJXD6FF,8;`Y4! YBy'Wb:ll;;`;\"JI0c2uvD':!LAk:s\"!'0.!2B55.T1VI?00Du?1,l``RFsc?Y?9vD5 K'3'1b!N8hn:'l. R:9:o`m1r.M2mrJ?`Wjv1`G6i6G`1vjW`?Jrm2M.r1m`o:::R .l':nh8N!b1'3'K 5Dv9?Y?csFR``l,1?uD00?IV1T.55B2!.0'!\"s:kAL!:'Dvu2c0IJ\";`;;ll9bW'yBY !4Y`;8,FF6DXJuJfOd`8Q1:X?P4'8;9")