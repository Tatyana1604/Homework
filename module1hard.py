students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students_list = list(students)
student_sort = sorted(students_list)
print(student_sort)
print(grades)
grades_average = [sum(sub_list) / len(sub_list) for sub_list in grades]
print(grades_average)
dictionary = dict(zip(sorted(students_list), grades_average))
print(dict(sorted(dictionary.items())))