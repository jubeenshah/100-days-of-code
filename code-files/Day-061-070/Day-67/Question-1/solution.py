numberOfElements = int(input())
setInput = set(map(int, input().split(" ")))
#print((setInput))

numberOfQueries = int(input())
for _ in range(numberOfQueries):
    query = input().split(" ")
    if query[0] == "pop":
        setInput.pop()
    elif query[0] == "remove":
        setInput.remove(int(query[1]))
    elif query[0] == "discard":
        setInput.discard(int(query[1]))
    else:
        print("what now?")
print(sum(setInput))

