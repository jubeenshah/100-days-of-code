# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

def printPoloarCoordinates(x,y):
    print(abs(complex(x,y)))
    print(cmath.phase(complex(x,y)))

complexInput = input()
isNegative = False
yNegative = False
if '+' in complexInput:
    #print("True")
    complexInput = complexInput.split('+')
    #print(complexInput)
if complexInput[0] == '-':
    isNegative = True
if '-' in complexInput:
    yNegative = True
    complexInput = complexInput.split('-')
    try:
        complexInput.remove('')
    except:
        pass
    #print(complexInput)
xValue,yValue = int(complexInput[0]),int(complexInput[1].split('j')[0])
#print(xValue, yValue)
if isNegative:
    xValue *= -1
if yNegative:
    yValue *= -1
#print(xValue,yValue)
printPoloarCoordinates(xValue,yValue)