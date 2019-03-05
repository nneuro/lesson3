# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

dicts = {}
for student in students:
    dicts.update({student.get('first_name'): students.count(student)})
for key in dicts.keys():
    print(f'{key.title()}:  {dicts.get(key)}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
# Пример вывода:
# Самое частое имя среди учеников: Маша

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
dicts = {}
for student in students:
    dicts.update({students.count(student): student.get('first_name')})
for key in dicts.keys():
    if key == max(dicts.keys()):
        print(f'Самое частое имя среди учеников: {dicts.get(max(dicts.keys()))}')
  


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
for class_list in school_students:
    dicts = {}
    for student in class_list:
        dicts.update({class_list.count(student): student.get('first_name')})
    for key in dicts.keys():
        if key == max(dicts.keys()):
            name_max = dicts.get(max(dicts.keys()))
    print(f'Самое частое имя в классе {school_students.index(class_list)+1} {name_max}')




# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]

is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for class_list in school:
    student_list_1 = class_list.get('students')
    girls = []
    boys = []
    for student in student_list_1:
        name = student.get('first_name')
        if is_male.get(name) == False:
            girls.append(name)
            
        elif is_male.get(name) == True:
            boys.append(name)
            
    print(f'В классе {class_list["class"]} {len(boys)} мальчиков и {len(girls)} девочки')
    


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек 
# и больше всего мальчиков.
# Пример вывода:
# Больше всего мальчиков в классе 3c

school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

girls_count_dict = {}
boys_count_dict = {}
for class_list in school:
    girls = []
    boys = []
    for student in class_list.get('students'):
        if is_male.get(student.get('first_name')) == False:
            girls.append(student.get('first_name'))
        elif is_male.get(student.get('first_name')) == True:
            boys.append(student.get('first_name'))
    girls_count_dict.update({len(girls):class_list["class"]})
    boys_count_dict.update({len(boys):class_list["class"]})
for count_girls, class_name in girls_count_dict.items():
    if count_girls == max(girls_count_dict.keys()):
        print(f'Больше всего девочек в классе {class_name}')
for count_boys, class_name in boys_count_dict.items():
    if count_boys == max(boys_count_dict.keys()):
        print(f'Больше всего мальчиков в классе {class_name}')

  

        
    