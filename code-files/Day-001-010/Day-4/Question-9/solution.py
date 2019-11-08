def timeConversion(s):
    s = s.split(":")
    am = False
    pm = False
    if "AM" in s[2]:
        #print("AM")
        am = True
    else:
        pm = True
        #print("PM")
    
    if pm:
        if s[0] != "12":
            s[0] = str(int(s[0]) + 12)
        
    if am:
        if s[0] == "12":
            s[0] = "0"+str(int(s[0]) - 12)
        
    s[2] = s[2][0:2]
        
    print(":".join(s))
timeConversion("12:45:54PM")