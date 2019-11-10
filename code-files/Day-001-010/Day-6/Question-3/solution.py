def gradingStudents(grades):
    newGrades = []
    for grade in grades:
        if grade < 38:
            newGrades.append(grade)
            continue
        else:
            if (((grade // 5) + 1) * 5) - grade < 3:
                grade = ((grade // 5) + 1) * 5
                newGrades.append(grade)
            else:
                newGrades.append(grade)
                
    print(grades)
    print(newGrades)

gradingStudents([73, 67, 38, 33])