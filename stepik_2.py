def index_weight(weight, height):
    index = weight/height ** 2
    if 18.25 <= index <= 25:
         print('Оптимальная масса')
    elif index < 18.25:
         print('Недостаточная масса')
    else:
        print('Избыточная масса')

a, b = float(input()), float(input())
index_weight(a, b)