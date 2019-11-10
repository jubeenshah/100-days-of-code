repeat = int(input())
for i in range(repeat):
    string = str(input())
    result = evenOdd(string)
    print(result)
    print()
    
def evenOdd(string) -> str:
    evenString = ''
    oddString = ''
    for x in range(len(string)):
        if x % 2 == 0:
            evenString += string[x]
        else:
            oddString += string[x]
        
    return (evenString+" " +oddString)