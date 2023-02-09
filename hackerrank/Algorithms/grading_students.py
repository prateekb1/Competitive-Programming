def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] > 37:
            if grades[i]%5 != 0:
                if (5-grades[i]%5 < 3):
                    grades[i] += 5-grades[i]%5
    return grades

print(gradingStudents([73, 67, 38, 33]))