def wrap(string, max_width):
    i = 0
    while i < len(string):
        print(string[i:i+max_width])
        i += max_width
    
    return

textWrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ",6)