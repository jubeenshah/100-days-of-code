listOfScores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    listOfScores.append([name,score])
scoreList = [i[1] for i in listOfScores]
secondHighest = (sorted(set(scoreList),reverse=True)[-2])

for i in sorted(listOfScores):
    if i[1] == secondHighest:
        print(i[0])