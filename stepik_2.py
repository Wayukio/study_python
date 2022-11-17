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

left = input() # Ввод левой части строки
right = left[::-1].replace('(', ')') # Правой строке присваиваем левую строку в обратном порядке (срез [::-1]) и методом replace меняем левые скобки на правые.
answer = left + right
print(answer)