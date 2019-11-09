def twoStrings(s1, s2):
    for char in s1:
        if char in s2:
            return "Yes"
        else:
            continue
    return "No"

twoStrings("hi","world")