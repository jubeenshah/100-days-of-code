# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
numberOfItems = int(input())
test_ordered_dict = OrderedDict()
#print(test_ordered_dict, "TEST")
for _ in range(numberOfItems):
    itemList = input().split(" ")
    cost = int(itemList[-1])
    itemName = ' '.join(itemList[0:len(itemList)-1])
    #print(cost, itemName,test_ordered_dict)
    if itemName not in test_ordered_dict:
        test_ordered_dict[itemName] = int(cost)
    else:
        test_ordered_dict[itemName] += int(cost)
for items in test_ordered_dict.items():
    print(items[0],items[1])