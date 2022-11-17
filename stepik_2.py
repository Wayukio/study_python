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

array = '5 6 2 4'.split()
array = list(map(int, array))
sum_ = 8
start = 0
finish = len(array)

while start < finish:
    for i in range(start + 1, finish):
        if array[start] + array[i] == sum_:
            answer = f'{start} {i}'
    start += 1

print(answer)