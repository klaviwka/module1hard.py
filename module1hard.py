grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
middle_grade_Aaron = sum(grades[0]) / len(grades[0])
middle_grade_Bilbo = sum(grades[1]) / len(grades[1])
middle_grade_Johnny = sum(grades[2]) / len(grades[2])
middle_grade_Khendrik = sum(grades[3]) / len(grades[3])
middle_grade_Steve = sum(grades[4]) / len(grades[4])
Result_grade_students = {'Aaron': int(middle_grade_Aaron),
                         'Bilbo': int(middle_grade_Bilbo),
                         'Johnny': int(middle_grade_Johnny),
                         'Khendrik': int(middle_grade_Khendrik),
                         'Steve': int(middle_grade_Steve)}
print(Result_grade_students)