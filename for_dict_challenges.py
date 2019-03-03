# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
student_list = []
for student in students:
    student_name = student.get('first_name') 
    student_list.append(student_name)

student_count_list = []
for student_name in student_list:
    student_name_count = student_list.count(student_name)
    student_count_list.append(student_name_count)

student_dict = dict( zip(student_list, student_count_list)) #удаляет повторы имён из списка
for key in student_dict.keys():
    print(f'{key.title()}:  {student_dict.get(key)}')

# {'Vasya': 1, 'Masha':2, ..}
#сделать словарь с имя: количество таких имён
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
# students = [
#   {'first_name': 'Вася'},
#   {'first_name': 'Петя'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Оля'},
# ]
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# school_students = [
#   [  # это – первый класс
    # {'first_name': 'Вася'},
    # {'first_name': 'Вася'},
#   ],
#   [  # это – второй класс
#     {'first_name': 'Маша'},
#     {'first_name': 'Маша'},
#     {'first_name': 'Оля'},
#   ]
# ]
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# school = [
#   {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
#   {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
# ]
# is_male = {
#   'Маша': False,
#   'Оля': False,
#   'Олег': True,
#   'Миша': True,
# }
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
# school = [
#   {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
#   {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
# ]
# is_male = {
#   'Маша': False,
#   'Оля': False,
#   'Олег': True,
#   'Миша': True,
# }
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
