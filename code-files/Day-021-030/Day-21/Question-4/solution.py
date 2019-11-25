def calculatePercent(student_marks:dict, query_name:str) -> float:
    #print(student_marks,query_name)
    #print(student_marks[query_name])
    return (sum(student_marks[query_name])/len(student_marks[query_name]))
x = calculatePercent(student_marks, query_name)
print('{:2.2f}'.format(x))
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x = calculatePercent(student_marks, query_name)
    print('{:2.2f}'.format(x))
    