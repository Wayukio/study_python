# def index_weight(weight, height):
#     index = weight/height ** 2
#     if 18.25 <= index <= 25:
#          print('Оптимальная масса')
#     elif index < 18.25:
#          print('Недостаточная масса')
#     else:
#         print('Избыточная масса')

# a, b = float(input()), float(input())
# index_weight(a, b)

# def is_valid_parentheses(par):
#     while True:
#         par2 = par.replace('()', '')
#         if par != par2:
#             par = par2
#         elif par == '':
#             return True
#         else:
#             return False

# par = ')(()))'
# print(is_valid_parentheses(par))

# end_simbol = ' !."№;%:?*()_-+=/\\}{][\'<>~`'
# text = input()
# add_word = 'ay'
# add_symbol = ''

# while text[-1] in end_simbol:
#     add_symbol += text[-1]
#     text = text[:-1]

# text = text.split()
# add_symbol = add_symbol[::-1]
# text = ' '.join([i[1:] + i[0] + add_word for i in text]) + add_symbol

# print(text)

# array = '5 6 2 4'.split()
# array = list(map(int, array))
# sum_ = 8
# start = 0
# finish = len(array)

# while start < finish:
#     for i in range(start + 1, finish):
#         if array[start] + array[i] == sum_:
#             answer = f'{start} {i}'
#     start += 1

# print(answer)

import re
import random


# input_data = input()
# Match = re.match(input_data, input_data)

# print(Match.group(), Match.start(), Match.end(), sep='\n')

# letter = input()
# greeting = r'Здравствуйте|Hello'
# check = re.match(greeting, letter)
# positive_answer = 'Ну привет!'
# negative_answer = 'Фу, как некультурно!'


# def answer_to_letter(check):
#     if check != None:
#         return positive_answer
#     return negative_answer

# print(answer_to_letter(check))

# names = ['Иоан', 'Платон', 'Омар', 'Ибрагим', 'Кеша']
# surnames = ['Феофанов', 'Жлобин', 'Золотов', 'Монпасье', 'Эмгыр']
# students = []


# def years_suffix(age):
#     if str(age)[-1] in '1':
#             age_suffix = 'год'
#     elif str(age)[-1] in '234':
#         age_suffix = 'года'
#     else:
#         age_suffix = 'лет'
#     return age_suffix

# class Person:
#     def __init__(self, name, surname, age, grades):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.grades = list(grades)

#     def __str__(self):
#         return f'{self.surname} {self.name}, {self.age}'

#     def greet(self):
#         age_suffix= years_suffix(self.age)
#         return f'Привет! Меня зовут {self.surname} {self.name}, мне {self.age} {age_suffix}.'


# def generate_students(count_stedents=5):
#     while len(students) != count_stedents:
#         students.append([random.choice(surnames), random.choice(names), random.randint(18, 25)])
#     return students

# man_1 = Person('Василий', 'Юдин', 23, [5, 5, 5, 5, 5])
# print(man_1)
# print(Person.greet(man_1))
# print(generate_students())


user_list = {}
answer_list = []
counter = 1

request = int(input())

def add_users_num(user):
    user += str(len(user_list[user]))
    return user

while request > 0:
    user = input()
    request -= 1
    if user not in user_list:
        answer_list.append('OK')
        user_list[user] = {user:user}
    else:
        user_num = add_users_num(user)
        user_list[user].setdefault(user_num, user_num)
        answer_list.append(user_num)
        

for answer in answer_list:
    print(answer)

print(user_list)