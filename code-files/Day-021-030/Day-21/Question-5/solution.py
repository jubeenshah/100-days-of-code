N = 2
listToReturn = []
for _ in range(N):
    line = input()
    line = line.split(' ')
    if line[0] == 'insert':
        listToReturn.insert(int(line[1]),int(line[2]))
    elif line[0] == 'print':
        print(listToReturn)
    elif line[0] == 'remove':
        listToReturn.remove(int(line[1]))
    elif line[0] == 'append':
        listToReturn.append(int(line[1]))
    elif line[0] == 'sort':
        listToReturn.sort()
    elif line[0] == 'pop':
        listToReturn.pop()
    else:
        listToReturn.reverse()