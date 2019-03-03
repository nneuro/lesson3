# Вывести последнюю букву в слове
# word = 'Архангельск'
# word_list = list(word)
# last_letter = word[-1]
# print(last_letter)


# Вывести количество букв а в слове
# word = 'Архангельск'
# a_count = word.count('а') + word.count('А')
# print(a_count)


# ???


# Вывести количество гласных букв в слове
# word = 'Архангельск'
# vowel_letters = ['а','е','у', 'А', 'Е']
# vow_list = []
# for letter in word:
#     for vow_letter in vowel_letters:
#         if letter == vow_letter:
#             vow = vow_letter
#             vow_list.append(vow)
# print(f'В слове Архангельск {len(vow_list)} буквы')


word = 'Архангельск'
vowel_letters = ['а','е','у', 'А', 'Е']
vow_list = []
for vowel_letter in vowel_letters:
    if vowel_letter in word:
        vow = vowel_letter
        vow_list.append(vow)
print(f'В слове Архангельск {len(vow_list)} буквы')
            
            
#  for vow_letter in word
# Вывести количество слов в предложении
# sentence = 'Мы приехали в гости'
# sentence_list = sentence.split()
# print(sentence_list)
# print(len(sentence_list))


# Вывести первую букву каждого слова на отдельной строке
# sentence = 'Мы приехали в гости'
# sentence_list = sentence.split()
# for word in sentence_list:
#     print(word[0])



# Вывести усреднённую длину слова.
# sentence = 'Мы приехали в гости'
# sentence_list = sentence.split()
# a_list = []
# for word in sentence_list:
#     a = len(word)
#     a_list.append(a)
# sentence_mean = sum(a_list)/len(a_list)
# print(sentence_mean)




# for a in score_list:
#     b=a['scores']
#     for el in b:
#         all.append(el)