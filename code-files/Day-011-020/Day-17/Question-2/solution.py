def catAndMouse(x, y, z):
    catAPos = x
    catBPos = y
    mousePos = z
    
    if abs(mousePos - catBPos) > abs(mousePos - catAPos):
        print("Cat A")
    elif abs(mousePos - catBPos) < abs(mousePos - catAPos):
        print("Cat B")
    else:
        print("Mouse C")

catAndMouse(1, 3, 2)