groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
for group in groups:
    aa = ', '.join(group)
    print(f'Группа {groups.index(group) + 1}: {aa}')






    # for i in range(0, len(group)):