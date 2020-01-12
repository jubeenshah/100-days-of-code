def intToString(n):
    dictOfIntToString = { 0: "Zero",
        1: "One",         2: "Two",             3: "Three",
        4: "Four",        5: "Five",            6: "Six",
        7: "Seven",       8: "Eight",           9: "Nine",
        10: "Ten",       11: "Eleven",         12: "Twelve",
        13: "Thirteen",  14: "Fourteen",       15: "Fifteen",
        16: "Sixteen",   17: "Seventeen",      18: "Eighteen",
        19: "Nineteen",  20: "Twenty",         30: "Thirty",
        40: "Fourty",    50: "Fifty",          60: "Sixty",
        70: "Seventy",   80: "Eighty",        90: "Ninety",
        100: "Hundred",1000: "Thousand", 1000000: "Million",
        1000000000: "Billion", 1000000000000: "Billion"
    }
    if n in dictOfIntToString:
        return dictOfIntToString[n]
    keys = [1000000000, 1000000, 1000, 100, 90, 80, 70,
               60, 50, 40, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12,
               11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    def dp(n):
        if n <= 20: return dictOfIntToString[n]
        for div in keys:
            d, r = divmod(n, div)
            if not d: continue
            s1 = dp(d) + " " if div >= 100 else ""
            s2 = " " + dp(r) if r else ""
            return s1 + dictOfIntToString[div] + s2

    return dp(n)
x = intToString(1230)
print(x)