def bonAppetit(bill, k, b):
    bobShouldveCharged = (sum(bill[:k]) + sum(bill[k+1:]))/2
    print(bobShouldveCharged)
    if bobShouldveCharged == b:
        print("Bon Appetit")
    else:
        print(int(b - bobShouldveCharged))

bonAppetit([3, 10, 2, 9],1,12)