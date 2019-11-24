import random
l1List = [random.randint(1,9) for i in range(1,5)]
print(l1List)
l2List = [random.randint(1,9) for i in range(1,5)]
print(l2List)
l1List.reverse()
l2List.reverse()

list1Length = len(l1List)-1
list2Length = len(l1List)-1

int1Val = 0
int2Val = 0


for element in l1List:
    #print(element,listLength,al1List)
    int1Val = int1Val + (element * 10**(list1Length))
    list1Length -=1
print(int1Val)   
for element in l2List:
    #print(element,listLength,l1List)
    int2Val = int2Val + (element * 10**(list2Length))
    list2Length -=1
print(int2Val)
print(int1Val+int2Val)
#print(intVal)