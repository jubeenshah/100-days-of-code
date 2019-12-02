# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

list1 = list(map(int, input().split(' ')))
list2 = list(map(int, input().split(' ')))

def iterTools(list1,list2):
    return (tuple(product(list1,list2)))

printTuple = iterTools(list1,list2)
for each in printTuple:
    print(each, end=" ")