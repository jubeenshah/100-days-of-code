def isPalindrome(x):
    n = x
    reverse = 0
    count = len(str(x))-1
    while x > 0:
        temp = x % 10
        x = x // 10
        reverse = reverse + (temp*10**count)
        count -= 1
    if n == reverse:
        print("true")
    else:
        print("false")
isPalindrome(-121121)