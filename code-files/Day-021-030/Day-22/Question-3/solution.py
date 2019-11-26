import re
def regexMatch(query, string):
    x = re.match(query,string)
    try:
        if x.start() == 0 and x.end() == len(string):
            print("True")
    except:
        print("False")

regexMatch("aa","a")