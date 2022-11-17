# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if a1 < a2 and a2 < b1 <= b2:
#     print(a2, b1)
# elif a2 <= a1 < b2 and b2 > b1 or a2 <= a1 < b2 and a2 < b1 < b2:
#     print(a1, b1)
# elif a1 < a2 and b1 < a2 or a1 > b2 and b1 > b2:
#     print('пустое множество')
# elif a1 < a2 and b1 == a2:
#     print(b1)
# elif a1 == b2 and b1 > b2:
#     print(a1)
# elif a1 < a2 < b1 and b2 < b1:
#     print(a2, b2)
# elif a2 < a1 < b2 and b2 <= b1:
#     print(a1, b2)

# year = int(input())
# if year % 100 == 0:
#     print('YES')
# else:
#     print('NO')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# ab1 = 0
# ab2 = 0
# if (a1 + b1) % 2 == 0:
#     ab1 = 1
# if (a2 + b2) % 2 == 0:
#     ab2 = 1
# if ab1 + ab2 == 1:
#     print('NO')
# else:
#     print('YES')

# age = int(input())
# sex = input()
# if 10 <= age <= 15 and sex == 'f':
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# if 0 < a <= 3:
#     print(a * 'I')
# elif a == 4:
#     print('IV')
# elif 5 <= a <= 8:
#     a = a - 5
#     print('V' + a * 'I')
# elif a == 9:
#     print('IX')
# elif a == 10:
#     print('X')
# else:
#     print('ошибка')

# a = int(input())
# if a % 2 == 0:
#     if 2 <= a <= 5 or a > 20:
#         print('NO')
#     elif 6 <= a <= 20:
#         print('YES')
# else:
#     print('YES')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if a1 - b1 == a2 - b2 or a1 + b1 == a2 + b2:
#     print('YES')
# else:
#     print('NO')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if (a1 + 2 == a2 and (b1 + 1 == b2 or b1 - 1 == b2)) or (a1 + 1 == a2 and (b1 + 2 == b2 or b1 - 2 == b2)) or (a1 - 2 == a2 and (b1 + 1 == b2 or b1 - 1 == b2)) or (a1 - 1 == a2 and (b1 + 2 == b2 or b1 - 2 == b2)):
#     print('YES')
# else:
#     print('NO')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if a1 - b1 == a2 - b2 or a1 + b1 == a2 + b2:
#     print('YES')
# elif a1 == a2 or b1 == b2:
#     print('YES')
# else:
#     print('NO')

# a, b = float(input()), float(input())
# print(a * b / 2)

# s, v1, v2 = float(input()), float(input()), float(input())
# print(s / (v1 + v2))

# a = float(input())
# print(1 / a if a != 0 else 'Обратного числа не существует')

# print((float(input())-32)*(5/9))

# d = float(input())
# i = 10.5
# h = i * d   
# if d > 2:
#     i = 4
#     h = h + (d - 2) * i
#     print(h)
# print(h)

# print(int(float(input()) * 10 % 10))

# print(float(input()) * 10000 % 10000 / 10000)

# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# print(f'Наименьшее число = {min(a, b, c, d, e)}', f'Наибольшее число = {max(a, b, c, d, e,)}', sep='\n')

# a, b, c = int(input()), int(input()), int(input())
# print(max(a, b, c), a + b + c - max(a, b, c) - min(a, b, c), min(a, b, c), sep='\n')

# a = input()
# a1 = int(a[0])
# a2 = int(a[1])
# a3 = int(a[2])
# if max(a1, a2, a3) - min(a1, a2, a3) == a1 + a2 + a3 - (min(a1, a2, a3) + max(a1, a2, a3)):
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# a1, a2, a3, a4, a5 = abs(float(input())), abs(float(input())), abs(float(input())), abs(float(input())), abs(float(input()))
# summ = a1 + a2 + a3 + a4 + a5
# print(summ)

# p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
# print(abs(p1 - q1) + abs(p2 - q2))

# print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

# print('Hello ' + (input()) + ' ' + (input()) + '! You just delved into Python')

# fc = input()
# print('Футбольная команда ' + fc + ' имеет длину ' + str(len(fc)) + ' символов')

# a, b, c = input(), input(), input()
# max = max(len(a), len(b), len(c))
# min = min(len(a), len(b), len(c))
# if len(a) == max:
#     max = a
# elif len(b) == max:
#     max = b
# else:
#     max = c
# if len(a) == min:
#     min = a
# elif len(b) == min:
#     min = b
# else:
#     min = c
# print(min, max, sep='\n')

# a, b, c = len(input()), len(input()), len(input())
# if a - b == b - c or a - c == c - b or c - a == a - b or c - b == b - a or b - a == a - c or b - c == c - a:
#     print('YES')
# else:
#     print('NO')

# a, b, c = len(input()), len(input()), len(input())
# print('YES' if (2 * a - b - c) * (2 * b - a - c) * (2 * c - a - b) == 0 else 'NO')


# print('YES' if 'синий' in input() else 'NO')

# day = input()
# print('YES' if 'суббота' in day or'воскресенье' in day else 'NO')

# mail = input()
# print('YES' if '@' in mail and '.' in mail else 'NO')

# from math import sqrt 
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
# p = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# print(p)


# from math import pow, pi

# r = float(input())
# s = pi * pow(r, 2)
# c = 2 * pi * r
# print(s, c, sep='\n')

# import math

# a, b = float(input()), float(input())
# sa = (a + b) / 2
# sge = math.sqrt(a * b)
# sga = (2 * a * b) / (a + b)
# sk = math.sqrt((pow(a, 2) + pow(b, 2)) / 2)
# print(sa, sge, sga, sk, sep='\n')


# from math import *

# x = radians(float(input()))
# z = sin(x) + cos(x) + pow(tan(x), 2)
# print(z)


# import math

# x = float(input())
# print(math.floor(x) + math.ceil(x))


# from math import sqrt, pow

# a, b, c = float(input()), float(input()), float(input())
# d = pow(b, 2) - 4 * a * c
# if d == 0:
#     print(-b / (2 * a))
# elif d > 0:
#     x1 = (-b + sqrt(d)) / (2 * a)
#     x2 = (-b - sqrt(d)) / (2 * a)
#     print(min(x1, x2), max(x1, x2), sep='\n')
# else:
#     print('Нет корней')


# import math

# n, a = float(input()), float(input())
# print((n * math.pow(a, 2)) / (4 * math.tan(math.pi / n)))


# for i in range(10):
#     print('Привет')

# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# for i in range (10):
#     print('Python is awesome!')

# t = input()
# for i in range(int(input())):
#     print(t)

# for _ in range (6):
#     print('A' * 3)
# for _ in range (5):
#     print('B' * 4)
# print('E')
# for _ in range (9):
#     print('T' * 5)
# print('G')

# for _ in range (int(input())):
#     print('*' * 19) 

# name = input()
# for i in range (10):
#     print(i, name)

# n = int(input())
# for i in range (n+1):
#     print(f'Квадрат числа {i} равен {i ** 2}')

# n = int(input())
# for i in range(n):
#     print('*' * n)
#     n = n - 1

# m, p, n = int(input()), int(input()), int(input())
# for i in range(n):
#     print(i + 1, m)
#     m = m + m * (p / 100)

# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     print(i)

# m, n = int(input()), int(input())
# if m <= n:
#     for i in range (m, n + 1):
#         print(i)
# else:
#     for i in range (m, n - 1, -1):
#         print(i)

# m, n = int(input()), int(input())
# for i in range(round(m + 0.5), n, -2):
#     print(i - 1)

# m, n = int(input()), int(input())
# for i in range(m, n):
#     if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
#         print(i)

# n = int(input())
# for i in range(1, 11):
#     print(n, 'x', i, '=', n * i)

# num = int(input())
# flag = True

# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False

# if num == 1:
#     print('Это единица, она не простая и не составная') 
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# import math

# a, b = int(input()), int(input())
# counter = 0
# for i in range(a, b + 1):
#     if math.pow(i, 3) % 10 == 4 or math.pow(i, 3) % 10 == 9:
#         counter += 1
# print(counter)

# n = int(input())
# total = 0
# for _ in range(n):
#     total += int(input())
# print(total)


# import math

# n = int(input())
# total = 1
# for i in range(2, n + 1):
#     total += 1/i
# print(total - math.log(n))

# n = int(input())
# total = 0
# for i in range(1, n):
#     if i % 5 == 0 and i % 10 != 0:
#         total += i
# print(total)


# import math

# print(math.factorial(int(input())))

# total = 1
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         total *= n
# print(total)

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     i *= (-1)**(i + 1)
#     total += i
# print(total)

# n = int(input())
# largest_max = int(input())
# largest_med = 0
# for i in range(n - 1):
#     largest_min = int(input())
#     if largest_min > largest_max:
#         largest_med = largest_max
#         largest_max = largest_min
#     if  largest_med < largest_min < largest_max:
#         largest_med = largest_min
# print(largest_max, largest_med, sep='\n')

# flag = True
# for i in range(10):
#     n = int(input())
#     if n % 2 == 1:
#         flag = False
# if flag:
#     print('YES')
# else:
#     print('NO')

# n, largest = int(input()), 0
# # print('1', end=' ')
# sum_pred = 1
# for i in range(1, n + 1):
#     print(sum_pred, end=', ')
#     smallest = largest
#     largest = sum_pred
#     sum_pred = smallest + largest

# word = input()
# slova = ''
# while word != 'КОНЕЦ':  
#     word2 = word
#     slova = slova + '\n' + word2
#     word = input()
# print(slova)

# word = input()
# while word != 'КОНЕЦ':
#     print(word)
#     word = input()

# word = input()
# while word != 'КОНЕЦ' and word != 'конец':
#     print(word)
#     word = input()

# word = input()
# total = 0
# while word not in('стоп', 'хватит', 'достаточно'):
#     total += 1
#     word = input()
# print(total)

# n = int(input())
# while n % 7 == 0:
#     print(n)
#     n = int(input())

# n = int(input())
# total = 0
# while n >= 0:
#     total += n
#     n = int(input())
# print(total)

# n = int(input())
# count = 0
# while n in range(1, 6):
#     if n % 5 == 0:
#         count += 1
#     n = int(input())
# print(count)

# m = int(input())
# count = 0
# while m // 25 > 0:
#     count += 1
#     m -= 25
# while m // 10 > 0:
#     count += 1
#     m -= 10
# while m // 5 > 0:
#     count += 1
#     m -= 5
# count += m
# print(count)

# m = int(input())
# total = m // 25 + (m % 25) // 10 + ((m % 25) % 10) // 5 + ((m % 25) % 10) % 5
# print(total)

# n = int(input())
# while n != 0:
#     m = n % 10
#     n //= 10
#     print(m)

# n = int(input())
# m = ''
# while n != 0:
#     m = str(n % 10)
#     n //= 10
#     print(m, end='')

# n = int(input())
# largest = n % 10
# smallest = largest
# while n != 0:
#     last = n % 10
#     if smallest > last:
#         smallest = last
#     if largest < last:
#         largest = last
#     n //= 10
# print(f'Максимальная цифра равна {largest}', f'Минимальная цифра равна {smallest}', sep='\n')


# n = int(input())
# total = 0 # сумма цифр
# counter = 0 # количество цифр
# product = 1 # произведение цифр
# n1 = n # запоминаем введенное число в другую переменную
# last_digit1 = n % 10 # находим последнюю цифру
# while n != 0: # пока n не равно 0
#     last_digit = n % 10 # находим последнюю цифру n
#     total += last_digit # суммируем последнюю цифру c оследним значением суммы
#     counter += 1 # считаем количество цифр прибавляя к прошлому значению + 1
#     product *= last_digit # находим произведение чисел умножая предыдущее значение на полсдежнюю цифру
#     n //=10 # делим число без остатка на 10
# average = total / counter # среднее арифметическое цифр числа
# first_digit = n1 // (10**(counter - 1)) # первая цифра
# f_l = first_digit + last_digit1 # сумма первой и последней цифры
# print(total, counter, product, average, first_digit, f_l, sep='\n') # печатаем все треюуемые переменные с переносом строки вместо пробела

# n = int(input())
# while n // 100 != 0:
#     n //= 10
# print(n % 10)

# n = int(input())
# total = 0
# count = 0
# while n != 0:
#     last_digit = n % 10
#     total += last_digit
#     count += 1
#     n //= 10
# if total / count == last_digit:
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# last_digit = n % 10
# total = 0
# count = 0
# while n != 0:
#     count += 1
#     if n % 10 == last_digit:
#         total += 1
#     n //= 10
# if count == total:
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# total = 0
# count = 0
# while n > 0:
#     count += 1
#     if n % 10 <= n // 10 % 10:
#         total += 1
#     n //= 10
# if count <= total + 1:
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break

# n = int(input())
# for i in range(1, n + 1):
#     if i in range(5, 10) or i in range(17, 38) or i in range (78, 88):
#         continue
#     print(i)

# mx = 0
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#     if x < mx:
#         mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')

# n = int(input())
# while n // 10 != 0:
#     n //= 10
# print(n)

#n = int(input())
#product = 1
#while n != 0:
    #digit = n % 10
    #product = product * digit
    #n //= 10
#print(product)
    
# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

# for i in range(9):
#     print(' ' * (4 - i), end='')
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# n = int(input())
# for i in range(n):
#     for i in range(3):
#         print(n, end=' ')
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(5):
#         print(i + 1, end=' ')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(f'{i} + {j} = {i + j}')
#     print()

# n = int(input())
# for i in range(n // 2 + 1):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
# for i in range(n // 2, 0, -1):
#     for j in range(i, 0, -1):
#         print('*', end='')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     print(str(i) * i)

# for n in range(14):
#     for k in range(13):
#         for m in range(12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print(n, k, m)

# for beef in range(10):
#     for cow in range(20):
#         for baby in range(200):
#             if beef * 10 + cow * 5 + baby * 0.5 == 100 and beef + cow + baby == 100:
#                 print(beef, cow, baby)




# for a in range(1, 150):
#     for b in range(a, 150):
#         for c in range(b, 150):
#             for d in range(c, 150):
#                 for e in range(d, 150):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5 and a < b < c < d < e:
#                         print(a + b + c + d + e)

# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 sum = a ** 5 + b ** 5 + c ** 5 + d ** 5
#                 e = int(sum ** (1/5))
#                 if sum == e ** 5:
#                     print(a, b, c, d, e)
#                     print(a + b + c + d + e)
#                     break

# n, k = int(input()), 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         k += 1
#         print(k, end=' ')
#     print()

# n, k = int(input()), 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         k += 1
#         print(k, end='')
#     for j in range(i + 1, 1, -1):
#         k -= 1
#         if k == 0:
#             break
#         print(k, end='')
#     print()

# m, n, tot, max_tot, max_nom = int(input()), int(input()), 0, 0, 0
# for i in range(m, n + 1):
#     tot = 0
#     for j in range(1, n +1):
#         if i % j == 0:
#             tot += j
#             if max_tot <= tot:
#                 max_tot = tot
#                 max_nom = i
# print(max_nom, max_tot)

# m = int(input())
# for i in range(1, m + 1):
#     tot = 0
#     for j in range(1, m +1):
#         if i % j == 0:
#             tot += 1
#     print(i, '+' * tot, sep='')
# print()

# n = int(input())
# if n > 9:
#     while n > 9:
#         tot = 0
#         while n != 0:
#             tot += n % 10
#             n //= 10
#         n = tot
#     print(tot)
# else:
#     print(n)

# import math 

# n = int(input())
# tot = 0
# for i in range(1, n + 1):
#     tot += math.factorial(i)
# print(tot)

# n = int(input())
# tot = 0
# prod = 1
# for i in range(1, n + 1):
#     prod = 1
#     for j in range(1, i + 1):
#         prod *= j
#     tot += prod
# print(tot)

# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     for j in range(m, i // 2):
#         if i % j != 0:
#             print(i)


# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     count = 0
#     for j in range(2, i + 1):
#         if i % j == 0:
#             count += 1
#     if count <= 1 and i != 1:
#         print(i)

# n = int(input())
# s = 0
# while n != 0:
#     if n % 2 == 0:
#         s += n % 10
#     n //= 10
# print(s)

# count = 0
# maximum = 0
# for i in range(8):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if abs(x) > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = int(input())
# b = '*' + ' ' * 17 + '*'
# a = '*' * 19
# for i in range(n):
#     if i == 0 or i == n - 1:
#         print(a)
#     else:
#         print(b)


# n = int(input())
# while n > 99:
#     last_dig = n % 10
#     n //= 10
# print(last_dig)

# print(input()[2])

# n = int(input())
# last = n % 10
# counter_3_dig = 0
# counter_last_dig = 1
# counter_chet = 0
# total_dig_more_5 = 0
# product_dig_more_7 = 1
# counter_dig_5_0 = 0
# while n != 0:
#     last_digit = n % 10
#     if last_digit == 3:
#         counter_3_dig += 1
#     if last_digit == last:
#         counter_last_dig += 1
#     if last_digit % 2 == 0:
#         counter_chet += 1
#     if last_digit > 5:
#         total_dig_more_5 += last_digit
#     if last_digit > 7:
#         product_dig_more_7 *= last_digit
#     if last_digit in (0, 5):
#         counter_dig_5_0 += 1
#     n //= 10
# print(counter_3_dig, counter_last_dig, counter_chet, total_dig_more_5, product_dig_more_7, counter_dig_5_0, sep='\n')




# for a in range(1, 33):
#     for b in range(1, 33):
#         for c in range(1, 33):
#             for d in range(1, 33):
#                 if  a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != b and a != c and a != d and b != c and b != d and c != d:
#                     print(a ** 3 + b ** 3)

# n = input()
# for i in range(0, len(n), 2):
#     print(n[i])

# n = input()
# tot = 0
# for i in range(0, len(n)):
#     tot += int(n[i])
# print(tot)

# text = input()
# for i in range(0, len(text)):
#     if text[i] in('0123456789'):
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')

# text = input()
# tot1 = 0
# tot2 = 0
# for i in text:
#     if i in '*':
#         tot1 += 1
#     if i in '+':
#         tot2 += 1
# print(f'Символ + встречается {tot2} раз', f'Символ * встречается {tot1} раз', sep='\n')

# text, tot = input(), 0
# for i in range(len(text)):
#     if i == len(text) - 1:
#         break
#     if text[i] in text[i + 1]:
#         tot += 1
# print(tot)

# text, gl, sogl = input(), 0, 0
# for i in text:
#     if i in('ауоыиэяЮюёЕе'):
#         gl += 1
#     if i in('бВвГгджзйклмНнпрСстфхцчшщ'):
#         sogl += 1
# print(f'Количество гласных букв равно {gl}', f'Количество согласных букв равно {sogl}', sep='\n')

# n = int(input())
# binar = ''
# last_digit = 0
# while n > 0:
#     last_digit = n % 2
#     binar += str(last_digit)
#     n //= 2
# for i in range(-1, -len(binar) - 1, -1):
#     print(binar[i], end='')

# txt = input()
# if len(txt) % 2 == 0:
#     if txt[:(len(txt)) // 2 - 1] in txt[:-(len(txt)) // 2 + 1:-1]:
#         print('YES')
#     else:
#         print('NO')
# else:
#     if txt[:(len(txt)) // 2] in txt[:-(len(txt)) // 2:-1]:
#         print('YES')
#     else:
#         print('NO')

# txt = input()
# for i in range(len(txt)):
#     if txt[i] in txt[-i - 1]:
#         continue
#     else:
#         print('NO')
#         break
# else:
#     print('YES')

# word = input()
# print(len(word), word * 3, word[:1], word[:3], word[-3:], word[::-1], word[1:-1], sep='\n')

# word = input()
# print(word[2], word[:-2:-1], word[:4], word[:-2], word[::2], word[1::2], word[::-1], word[::-2], sep='\n')

# word = input()
# if len(word) % 2 == 0:
#     word = word[len(word) // 2:] + word[:len(word) // 2]
# else:
#     word = word[(len(word) + 1) // 2:] + word[:(len(word) + 1) // 2]
# print(word)

# words, answer = input(), 'NO'
# if words == words.title():
#     answer = 'YES'
# print(answer)

# word = input()
# print(word.swapcase())

# word, answer = input(), 'NO'
# if 'хорош' in word.lower():
#     answer = 'YES'
# print(answer)

# word, total = input(), 0
# for i in word:
#     if i == i.lower() and i.swapcase() != i.lower():
#         total += 1
# print(total)

# words = input()
# print(words.count(' ') + 1)

# letters = input()
# s_letters = letters.lower()
# print(f'Аденин: {s_letters.count("а")}', f'Гуанин: {s_letters.count("г")}', f'Цитозин: {s_letters.count("ц")}', f'Тимин: {s_letters.count("т")}', sep='\n')

# n = int(input())
# total = 0
# for i in range(n):
#     words = input()
#     if words.count('11') >= 3:
#         total += 1
# print(total)


# words = input()
# tot_count = 0
# for i in range(0, len(words)):
#     if words[i] in('0123456789'):
#         tot_count += words.count(words[i])
# print(tot_count)


# txt = input()
# answer = 'NO'
# okay = ('.com', '.ru')
# if txt.endswith(okay):
#     answer = 'YES'
# print(answer)

# txt = input()
# total = 0
# count = 0
# max_count = 0
# max_i_count = ''
# for i in range(len(txt)):
#     count = 0
#     if txt.startswith(txt[i]):
#         count += 1
#         if count >= max_count:
#             max_count = count
#             max_i_count = txt[i]
# print(txt[i])

# txt = input()
# max_count = 0
# for i in range(len(txt)):
#     if txt.count(txt[i]) > max_count:
#         max_count += txt.count(txt[i])
#         max_i_count = txt[i]
# print(max_i_count)

# txt = input()
# if 0 <= txt.find('f') < txt.rfind('f'):
#     print(txt.find('f'), txt.rfind('f'))
# elif 0 <= txt.find('f') == txt.rfind('f'):
#     print(txt.find('f'))
# else:
#     print('NO')

# txt = input()
# txt_edit = txt.replace(txt[txt.find('h') : txt.rfind('h') + 1], '')
# print(txt_edit)

# for i in range(int(input()), int(input()) + 1):
#     print(chr(i), end=' ')

# text = input()
# for i in range(len(text)):
#     print(ord(text[i]), end=' ')

# shift = int(input())
# words = input()
# for i in range(len(words)):
#     if ord(words[i]) - shift < 97:
#         print(chr(122 - (shift - (ord(words[i]) - 97))), end='')
#         continue
#     print(chr(ord(words[i]) - shift), end='')

# n = input()
# for i in range(0, len(n)):
#     if i % 3 != 0:
#         print(n[i], end='')


# print(input().replace('1', 'one')) 

# print(input().replace('@', ''))

# word = input()
# answer = -2
# if word.find('f') > -1:
#     if word.find('f', (word.find('f') + 1)) >= -1:
#         answer = word.find('f', (word.find('f') + 1))
# print(answer)

# word = input()
# w_swap = word[(word.rfind('h')) : (word.find('h')) : -1]
# complete_word = word[:(word.find('h'))] + w_swap + word[(word.rfind('h')) + 1:]
# print(complete_word)

# n = int(input())
# print(list(range(1, n + 1)))

# n = int(input())
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(list(abc[:n]))

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 
# 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 
# 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# answer = 'NO'
# if [5, 17] in numbers:
#     answer = 'YES'
# print(len(numbers), numbers[-1], numbers[::-1], answer, numbers[1:-1], sep='\n')

# my_list = []
# for _ in range(int(input())):
#     my_list.append(input())
# print(my_list)

# this_list = []
# for i in range(1, 27):
#     this_list.append(chr((ord('a') + i - 1)) * i)
# print(this_list)

# list = []
# for i in range(int(input())):
#     list.append(int(input()) ** 3)
# print(list)

# list = []
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         list.append(i)
# print(list)

# list = []
# n = int(input())
# summ = 0
# count = 0
# for i in range(n):
#     m = int(input())
#     summ += m
#     count += 1
#     if count == 2:
#         count = 1
#         list.append(summ)
#         summ = m
# print(list)

# lst = []
# n = int(input())
# for _ in range(n):
#     lst.append(int(input()))
# del lst[1::2]
# print(lst)

# lst = []
# n = int(input())
# for _ in range(n):
#     lst.append(input())
# k = int(input())
# for i in range(n):
#     if len(lst[i]) >= k:
#         print((lst[i])[k - 1], end='')

# lst = []
# n = int(input())
# for _ in range(n):
#     lst.extend(input())
# print(lst)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] ** 2
# print(sum(numbers))

# lst = []
# lst2 = []
# n = int(input())
# for i in range(n):
#     x = int(input())
#     lst.append(x)
#     lst2.append(x ** 2 + x * 2 + 1)
# print(*lst, '', *lst2, sep='\n')

# lst = []
# n = int(input())
# for _ in range(n):
#     lst.append(int(input()))
# del lst[lst.index(max(lst))]
# del lst[lst.index(min(lst))]
# print(*lst, sep='\n')


# n = int(input())
# lst = [input()]
# for i in range(1, n):
#     x = input()
#     if x not in lst:
#         lst.append(x)
#     else:
#         continue
# print(*lst, sep='\n')

# n = int(input())
# lst = []
# lst2 = []
# lst_l = []
# for i in range(n):
#     x = input()
#     lst.append(x)
#     lst_l.append(x.lower())
# quest = input().lower()
# for j in range(n):
#     if quest in lst_l[j]:
#         lst2.append(lst[j])
# print(*lst2, sep='\n')

# count_str = int(input())
# list_quest = []
# list_quest_complete = []
# list_quest_mini = []
# quest_lst = []
# for _ in range(count_str):
#     x = input()
#     list_quest.append(x)
#     list_quest_mini.append(x.lower())
# count_word = int(input())
# for _ in range(count_word):
#     quest = input().lower()
#     quest_lst.append(quest)
# for i in range(count_str):
#     for j in range(count_word):
#         if quest_lst[j] in list_quest_mini[i]:
#             flag = True
#         else:
#             flag = False
#             break
#     if flag:
#         list_quest_complete.append(list_quest[i])
# print(*list_quest_complete, sep='\n')

# lst_all = []
# negatives = []
# zero = []
# pozitives = []
# n = int(input())
# for i in range(n):
#     integ = int(input())
#     if integ < 0:
#         negatives.append(integ)
#     if integ == 0:
#         zero.append(integ)
#     if integ > 0:
#         pozitives.append(integ)
# lst_all.extend(negatives)
# lst_all.extend(zero)
# lst_all.extend(pozitives)
# print(*lst_all, sep='\n')


# print(*input().split(), sep='\n')

# fio = []
# for i in input().split():
#     fio.append(i[0])
# print('.'.join(fio) + '.')


# print(*input().split(chr(92)), sep='\n')

# nums = input().split()
# for i in range(len(nums)):
#     print((int(nums[i]) * '+'))

# n = input().split('.')
# answer = 'ДА'
# for i in range(len(n)):
#     if 0 > int(n[i]) or int(n[i]) > 255:
#         answer = 'НЕТ'
#         break
# print(answer)

# word = input()
# print(input().join(word))

# digits = input().split()
# count = 0
# for i in range(len(digits)):
#     for j in range(i + 1, len(digits)):
#         if digits[i] == digits[j]:
#             count += 1
# print(count)

# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers.extend(numbers.copy())
# numbers.insert(3, 25)
# print(numbers)

# n = input().split()
# for i in range(len(n)):
#     n[i] = int(n[i])
# min_n = min(n)
# max_n = max(n)
# if n.index(min(n)) < n.index(max(n)):
#     n[n.index(max(n))] = min_n
#     n[n.index(min(n))] = max_n
# else:
#     n[n.index(min(n))] = max_n
#     n[n.index(max(n))] = min_n
# print(*n)

# text = input().lower().split()
# print('Общее количество артиклей:', text.count('a') + text.count('an') + text.count('the'))

# n = input()
# n = n[1:]
# n = int(n)
# code_lst = []
# for i in range(n):
#     code = input().split(' ')
#     if '' in code:
#         if '' in code[:4]:
#             del code[code.index(''):4]
#             if '' in code:
#                 del code[code.index(''):]
#             code.insert(0, '   ')
#         elif '' in code[4:]:
#             del code[code.index(''):]
#     code_lst.append(code)
# for j in range(len(code_lst)):
#     print(*code_lst[j])

# n = input()
# n = n[1:]
# n = int(n)

# code_lst = []

# for i in range(n):
#     code = input().split(' ')
#     step_list = []
#     for k in range(len(code)):
#         step_list.extend(code[k])
#         if '#' in step_list:
#             del step_list[step_list.index('#'):]
#             break
#     code_lst.append(''.join(step_list))
# print(*code_lst, sep='\n')


#     s = ' '.join(code)
#     # code = s.rstrip
#     code_lst.append(s)
# # for j in range(len(code_lst)):
# print(*code_lst, sep='\n')

# n = input()
# n = n[1:]
# n = int(n)

# code_lst = []

# for i in range(n):
#     code = input().split(' ')
#     for j in range(len(code)):
#         if '#' in code[j]:
#             del code[j:]
#             break
#     code = ' '.join(code)
#     code = code.rstrip()
#     code_lst.append(code)
# print(*code_lst, sep='\n')

# a = input().split()
# for i in range(len(a)):
#     a[i] = int(a[i])
# a.sort()
# b = a.copy()
# b.sort(reverse = True)
# for j in range(len(a)):
#     a[j] = str(a[j])
#     b[j] = str(b[j])
# a = ' '.join(a)
# b = ' '.join(b)
# print(a, b, sep='\n')



# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [i[1:] for i in keywords]

# print(new_keywords)



# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# lengths = [len(i) for i in keywords]

# print(lengths)



# palindromes = [i for i in range(101, 1000) if str(i)[0] == str(i)[-1]]

# print(palindromes)


# print(*[i ** 2 for i in range(1, int(input()) + 1)], sep='\n')

# n = input().split()
# m = [int(i) ** 3 for i in n]
# print(*m)

# words = [i for i in input().split()]
# print(*words, sep='\n')

# print(*[i for i in input() if i.isdigit()], sep='')

# n = [int(i) ** 2 for i in input().split() if i.isdigit() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4]
# print(*n) 

# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88,-16, -78,
# 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6,
# 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25,
# 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16,
# 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21,
# -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

# n = len(a)
# flag = True
# for i in range(n - 1):
#     if flag == False:
#         break
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = True
#         else:
#             flag = False

# print(a)


# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94,
# -47,57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96,
# 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56,
# 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39,
# 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87,
# 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

# n = len(a)

# # реализация алгоритма сортировки выбором
# for i in range(n):
#     a[a.index(max(a[:n - i]))], a[n - i - 1] = a[n - i - 1], a[a.index(max(a[: n - i]))]

# print(a)

# print([i for i in range(2, int(input()) + 1, 2)])

# l = input().split()
# m = input().split()
# a = len(l)
# o = [int(l[i]) + int(m[i]) for i in range(a)]
# print(*o)

# val = input().split()
# val_sum = sum([int(val[i]) for i in range(len(val))])
# print(*val, sep='+', end=f'={val_sum}')


# print(max([len(i) for i in input().split()]))


# print(*[i[1:] + i[0] + 'ки' for i in input().split()])



# number = input().split('-')
# number_len = [len(i) for i in number if (i.isdigit() or i == '-')]
# answer = 'NO'
# if number_len == [3, 3, 4] or (number_len == [1, 3, 3, 4] and int(number[0]) == 7):
#         answer = 'YES'
# for i in number:
#     if i.isalpha():
#         answer = 'NO'
# print(answer)


# def draw_box():
#     for i in range(14):
#         if 0 < i < 13:
#             print('*' + ' ' * 8 + '*')
#         else:
#             print('*' * 10)

# # основная программа
# draw_box()  # вызов функции


# # объявление функции
# def draw_triangle():
#     for i in range(10):
#         print((i + 1) * '*')

# # основная программа
# draw_triangle()  # вызов функции


# def draw_triangle(fill, base):
#     for i in range(1, base + 1):
#         if i * 2 <= base + 1:
#             print(fill * i)
#         else:
#             print(fill * (base + 1 - i))


# draw_triangle(input(), int(input()))


# def print_fio(name, surname, patronymic):
#     for i in (name, surname, patronymic):
#         i = i[0]
#         print(i.upper(), end='')


# name, surname, patronymic = input(), input(), input()


# print_fio(surname, name, patronymic)



# def print_digit_sum(num):
#     print(sum([int(i) for i in str(num)]))


# n = int(input())


# print_digit_sum(n)


# def convert_to_miles(km):
#     return km * 0.6214


# num = int(input())


# print(convert_to_miles(num))


# def get_days(month):
#     if month in range(1, 8, 2) or month in range(8, 13, 2):
#         days = 31
#     if month in range(2, 7, 2) or month in range(9, 12, 2):
#         days = 30
#         if month == 2:
#             days = 28
#     return days


# num = int(input())

# print(get_days(num))


# def get_factors(num):
#     factors = [i for i in range(1, num + 1) if num % i == 0]
#     return factors


# n = int(input())

# print(get_factors(n))


# def number_of_factors(num):
#     return len(get_factors(num))


# n = int(input())

# print(number_of_factors(n))


# def find_all(target, symbol):
#     finder = [target.find(symbol, i) for i in range(len(target)) if target.find(symbol, i) != target.find(symbol, i + 1)]
#     return finder

    
# s = input()
# char = input()

# print(find_all(s, char))


# def merge(list1, list2):
#     list1.extend(list2)
#     list1.sort()
#     return list1
    


# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]

# print(merge(numbers1, numbers2))


# def quick_merge(list1, list2):
#     result = []

#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2

#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1

#     if p1 < len(list1):   # прицепление остатка
#         result += list1[p1:]
#     if p2 < len(list2):
#         result += list2[p2:]
    
#     return result


# def merge_lists_2(n):
#     lst = []
#     for _ in range(n):
#         mk = [int(i) for i in input().split()]
#         lst = quick_merge(lst, mk)
#     return lst
    


# n = int(input())
# print(*merge_lists_2(n))


# def is_valid_triangle(side1, side2, side3):
#     if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
#         return True
#     else:
#         return False


# a, b, c = int(input()), int(input()), int(input())
# print(is_valid_triangle(a, b, c))


# def is_prime(num):
#     sum_split = sum([i for i in range(1, (num + 1) // 2) if num % i == 0])
#     if sum_split > 1 or num == 1:
#         return False
#     else:
#         return True


# # n = int(input())
# # print(is_prime(n))


# def get_next_prime(num):
#     while True:
#         num += 1
#         if is_prime(num):
#             return num


# n = int(input())
# print(get_next_prime(n))


# def is_password_good(password):
#     if len(password) >= 8:
#         if not password.islower() and not password.isupper():
#             if password.isalnum() and not password.isalpha() and not password.isdigit():
#                 return True
#             else:
#                 return False    
#         else:
#             return False        
#     else:
#         return False


# txt = input()
# print(is_password_good(txt))


# def is_one_away(word1, word2):
#     count = 0
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] == word2[i]:
#                 count += 1
#         if count + 1 == len(word1):
#             return True
#         else:
#             return False
#     else:
#         return False


# txt1 = input()
# txt2 = input()
# print(is_one_away(txt1, txt2))


# def is_palindrome(text):
#     text = text.lower()
#     n = len(text)
#     text = [text[j] for j in range(n) if text[j] not in (' ,.!?-')]
#     text = ''.join(text)
#     n = len(text)
#     answer = True
#     for i in range(n):
#         if text[i] != text[n - 1 - i]:
#             answer = False
#     return answer


# txt = input()
# print(is_palindrome(txt))


# def is_prime(num2):
#     sum_split = sum([i for i in range(1, (num2 + 1) // 2) if num2 % i == 0])
#     if sum_split > 1 or num2 == 1:
#         return False
#     else:
#         return True


# def is_palindrome(num1):
#     num1 = str(num1)
#     n = len(num1)
#     answer = True
#     for i in range(n):
#         if num1[i] != num1[n - 1 - i]:
#             answer = False
#     return answer


# def is_even(num3):
#     if num3 % 2 == 0:
#         return True
#     else:
#         return False


# def is_valid_password(password):
#     list_password = [int(i) for i in password.split(':')]
#     if len(list_password) < 4:
#         if is_palindrome(list_password[0]):
#             if is_prime(list_password[1]):
#                 if is_even(list_password[2]):
#                     return True
#                 else:
#                     return False
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False


# psw = input()
# print(is_valid_password(psw))


# def is_correct_bracket(text):
#     n = len(text)
#     total = 0
#     answer = False
#     for i in range(n):
#         if text[i] == '(':
#             total += 1
#         else:
#             total -= 1
#         if total < 0:
#             break
#     if total == 0:
#         answer = True
#     else:
#         answer = False
#     return answer


# txt = input()
# print(is_correct_bracket(txt))



# def convert_to_python_case(text):
#     snake_case = [i for i in text]
#     for j in range(len(snake_case) - 1, 0, -1):
#         if snake_case[j].isupper():
#             snake_case.insert(j, '_')
#     snake_case = ''.join(snake_case)
#     return snake_case.lower()


# txt = input()
# print(convert_to_python_case(txt))


# def get_middle_point(x1, y1, x2, y2):
#     middle_x = (x1 + x2) / 2
#     middle_y = (y1 + y2) / 2
#     return middle_x, middle_y


# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())

# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# from math import pi


# def get_circle(radius):
#     c = 2 * pi * radius
#     s = pi * radius ** 2
#     return c, s


# r = float(input())

# length, square = get_circle(r)
# print(length, square)


# def solve(a, b, c):
#     d = b ** 2 - 4 * a * c
#     x1 = (-b + d ** 0.5)/(2 * a)
#     x2 = (-b - d ** 0.5)/(2 * a)
#     return min(x1, x2), max(x1, x2)


# a, b, c = int(input()), int(input()), int(input())

# x1, x2 = solve(a, b, c)
# print(x1, x2)


# def draw_triangle():
#     heigh = 8
#     width = 15
#     space = ' '
#     k = 1
#     for i in range(1, heigh + 1):
#         space = ((width + 1) // 2 - i) * ' '
#         for j in range(k, width + 1):
#             stars = j * '*'
#             k += 2
#             break
#         print(space + stars)


# draw_triangle()


# def get_shipping_cost(quantity):
#     shipping_cost = 0
#     for i in range(quantity):
#         if i == 0:
#             shipping_cost += 1000
#         else:
#             shipping_cost += 120
#     return shipping_cost



# n = int(input())
# print(get_shipping_cost(n))


# from math import factorial


# def compute_binom(n, k):
#     binom = (factorial(n)) / (factorial(k) * factorial(n - k))
#     return int(binom)


# n = int(input())
# k = int(input())


# print(compute_binom(n, k))


# def number_to_words(num):
#     digit_1_9_list = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#     digit_11_19_list = ['один', 'две', 'три', 'четыр', 'пят', 'шест', 'сем', 'восем', 'девят']
#     digit_10_90_list = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if num in range(1, 10):
#         words = digit_1_9_list[num - 1]
#     if num in range(11, 20):
#         words = digit_11_19_list[num % 10 - 1] + 'надцать'
#     if num == 10 or num in range(20, 100):
#         words = digit_10_90_list[num // 10]
#         num %= 10
#         if num > 0:
#             words += ' ' + digit_1_9_list[num - 1]
#     return words


# n = int(input())
# print(number_to_words(n))


# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#     if language == 'en':
#         return lng_en[number - 1]
#     else:
#         return lng_ru[number - 1]


# lan = input()
# num = int(input())

# print(get_month(lan, num))


# def is_magic(date):
#     answer = False
#     magic_list = [int(i) for i in date.split('.')]
#     if magic_list[0] * magic_list[1] == magic_list[2] % 100:
#         answer = True
#     return answer


# date = input()
# print(is_magic(date))


# def is_pangram(text):
#     abc_text = 'qwertyuiopasdfghjklzxcvbnm'
#     for i in range(len(abc_text)):
#         if abc_text[i] in text.lower():
#             answer = True
#         else:
#             answer = False
#             break
#     return answer


# text = input()
# print(is_pangram(text))




# ███╗░░░███╗██╗███╗░░██╗██╗  ██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗░██████╗
# ████╗░████║██║████╗░██║██║  ██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝
# ██╔████╔██║██║██╔██╗██║██║  ██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░╚█████╗░
# ██║╚██╔╝██║██║██║╚████║██║  ██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░░╚═══██╗
# ██║░╚═╝░██║██║██║░╚███║██║  ██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░██████╔╝
# ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░╚═════╝░


import random

# def throw_cube():
#     firs_cube = 'Перый кубик ' + str(random.randint(1, 6))
#     second_cube = 'Второй кубик ' + str(random.randint(1, 6))
#     print(firs_cube, second_cube, sep='\n')

# def throw_coin():
#     coin = random.randint(0, 1)
#     if coin == 0:
#         coin = 'Орёл'
#     else:
#         coin = 'Решка'
#     print(coin)

# def amount_throw_coin(n):
#     for _ in range(n):
#         throw_coin()

# def random_list_1_100():
#     numbers = [i for i in range(1, 101)]
#     random.shuffle(numbers)
#     return numbers


### GAME UGADAYKA ###
# def random_num_in_list():
#     num = random.choice(random_list_1_100())
#     return num

# def random_some_num_in_list():
#     count_nums = random_num_in_list()
#     print(count_nums)
#     random_nums = random.sample(random_list_1_100(), count_nums)
#     return random_nums

# def counting_score(counter):
#     if counter in range(1, 8):
#         score = 100
#     else:
#         score = 100 - (counter - 7)
#     return score

# def is_valid(n):
#     if n.isdigit() and 1 <= int(n) <= 100:
#         return True
#     else:
#         return False

# def game_ugadayka():
#     print('Добро пожаловать в числовую угадайку!')
#     number = random_num_in_list()
#     count_attempt = 0
#     while True:
#         n = input('Введите число от 1 до 100 и нажмите клавишу "Enter": ')
#         if is_valid(n):
#             count_attempt += 1
#             n = int(n)
#         else:
#             print('Сработала защита от дурака... Введите, пожалуйста ЦЕЛОЕ ЧИСЛО, в диапазоне ОТ 1 ДО 100!')
#             continue
#         if n == number:
#             score = counting_score(count_attempt)
#             print('Вы угадали, поздравляем!', '', f'Количество попыток: {count_attempt}', f'Заработано очков: {score}', sep='\n')
#             print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
#             break
#         elif n > number:
#             print(random.choice(['Слишком много, попробуйте еще раз', 'СЛИШКОМ БОЛЬШОЕ ЧИСЛО', 'Выбери число поменбше...']))
#             print('')
#             continue
#         else:
#             print(random.choice(['Слишком мало, попробуйте еще раз', 
#             'Увы и ах, но число которое вы ввели оказалось нестерпимо маловатым, в сравнении с тем, что было загадано', 
#             'Это число малюська']))
#             print('')
#             continue

# def attempt_guess_number(n):
    # counter = 0
    # while n != 1:
    #     counter += 1
    #     if n != 1:
    #         if n % 2 != 0:
    #             n += 1        
    #     n //= 2
    # return counter


##### MAGIC BALL #####
# answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", 
# "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", 
# "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", 
# "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]

# pre_answers = ["Хмммм, я думаю что мой ответ...", "Внимай в мое слово...", "Лучший ответ на твой вопрос..."]

# questions = ["Что таится внутри тебя? Задай вопрос:", "Есть такой вопрос, который интересен тебе? Спроси:", "Я отвечу на любой вопрос, просто напиши его сюда:"]

# def greeting_magic_ball():
#     print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос...')
#     name = input("Назовись, смертная душа: ")
#     print(f'Приветствую тебя, {name}!!!')

# def end_scene():
#     print('Желаете ли вы вновь получить ответ на свой вопрос? Ответьте, "Да" или "Нет":', end=' ')
#     while True:
#         restart = input().lower()
#         if restart.isalpha() and restart in ['да', 'нет']:
#             if restart == 'да':
#                 return True
#             else:
#                 return False
#         else:
#             print('ВСЕГО ДВА ВАРИАНТА ОТВЕТА!!! Попробуйте снова:', end=' ')
#             continue

# def answer_magic_ball():
#     greeting_magic_ball()
#     while True:
#         answer = random.choice(answers)
#         print(random.choice(questions))
#         quest = input()
#         print(random.choice(pre_answers), answer)
#         if end_scene() == True:
#             continue
#         else:
#             print(f'До скорых встреч, мы еще увидимся... А если нет, то я это прдесказал!!!')
#             break

### Password Generator ###
# digits = '0123456789'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# punctuation = '!#$%&*+-=?@^_'

# def is_validation_count_len(n):
#     while True:
#         if n.isdigit():
#             return True
#         else:
#             return False

# def is_validation_yes_no(ans):
#     while True:
#         if ans in ['да', 'нет']:
#             return True
#         else:
#             return False

# def pasword_count_information():
#     while True:
#         count_passwords = input('Введите количество паролей для генерации: ')
#         if is_validation_count_len(count_passwords):
#             count_passwords = int(count_passwords)
#             return count_passwords
#         else:
#             print('Введите коректные даные (число)')
#             continue

# def pasword_length_information():
#     while True:
#         len_one_password = input('Введите длину одного пароля: ')
#         if is_validation_count_len(len_one_password):
#             len_one_password = int(len_one_password)
#             return len_one_password
#         else:
#             print('Введите коректные даные (число)')
#             continue

# def pasword_chars_information():
#     while True:
#         while True:
#             digg = input('Должны ли быть цифры? Ответьте, "да" или "нет": ').lower()
#             if is_validation_yes_no(digg):
#                 break
#             else:
#                 print('Только "да" или "нет" Попробуйте снова:', end=' ')
#                 continue
#         while True:
#             alph_upper = input('Должны ли быть БОЛЬШИЕ БУКВЫ? Ответьте, "да" или "нет": ').lower()
#             if is_validation_yes_no(alph_upper):
#                 break
#             else:
#                 print('Только "да" или "нет" Попробуйте снова:', end=' ')
#                 continue
#         while True:
#             alph_lower = input('Должны ли быть маленькие буквы? Ответьте, "да" или "нет": ').lower()
#             if is_validation_yes_no(alph_lower):
#                 break
#             else:
#                 print('Только "да" или "нет" Попробуйте снова:', end=' ')
#                 continue
#         while True:
#             good_simbol = input('Должны ли быть символы (!#$%&*+-=?@^_)? Ответьте, "да" или "нет": ').lower()
#             if is_validation_yes_no(good_simbol):
#                 break
#             else:
#                 print('Только "да" или "нет" Попробуйте снова:', end=' ')
#                 continue
#         while True:
#             bad_simbol = input('Исключить ли неоднозначные символы (il1Lo0O)? Ответьте, "да" или "нет": ').lower()
#             if is_validation_yes_no(bad_simbol):
#                 break
#             else:
#                 print('Только "да" или "нет" Попробуйте снова:', end=' ')
#                 continue
#         list_answer = [digg, alph_upper, alph_lower, good_simbol, bad_simbol]
#         if 'да' not in list_answer[:-1]:
#             print('Вы не выбрали символов. Генерация невозможна, попробуйте еще раз.')
#             continue
#         else:
#             break
#     return list_answer

# def chars_complete():
#     chars = ''
#     list_answer = pasword_chars_information()
#     if list_answer[0] == 'да':
#         chars += digits
#     if list_answer[1] == 'да':
#         chars += uppercase_letters
#     if list_answer[2] == 'да':
#         chars += lowercase_letters
#     if list_answer[3] == 'да':
#         chars += punctuation
#     if list_answer[4] == 'да':
#         for i in 'il1Lo0O':
#             chars = chars.replace(i, '')
#     return chars

# def generate_password(length, chars):
#     count = pasword_count_information()
#     for j in range(count):
#         password = ''
#         while len(password) < length:
#             password += random.choice(chars)
#         print(password)

# length = pasword_length_information()
# chars = chars_complete()
# generate_password(length, chars)

### Caezar cipher ###
# rus_al_up = [chr(ord('А') + i) for i in range(32) if chr(ord('А') + i) != 'Ё']
# rus_al_low = [chr(ord('а') + i) for i in range(32) if chr(ord('А') + i) != 'ё']
# en_al_up = [chr(ord('A') + i) for i in range(26)]
# en_al_low = [chr(ord('a') + i) for i in range(26)]

# def direction_cipher():
#     while True:
#         txt = input('Шифруем или дешифруем текст? Ответьте "+", если шифруем и "-", если дешифруем: ')
#         if txt in ['+', '-']:
#             return txt
#         else:
#             print('Вы ввели некорректные данные, попробуйте еще раз.')

# def select_language():
#     while True:
#         txt = input('Выберите язык шифруемого текста. Ответьте "Рус", если "Русский" и "Eng", если "Английский": ').lower()
#         if txt in ['рус', 'eng']:
#             return txt
#         else:
#             print('Вы ввели некорректные данные, попробуйте еще раз.')

# def step_direction():
#     while True:
#         step = input('Введите шаг сдвига (число): ')
#         if step.isdigit():
#             step = int(step)
#             return step
#         else:
#             print('Вы ввели некорректные данные, попробуйте еще раз.')

# def caesar_ciphr():
#     text = input('Введите текст, который нужно изменить: ')
#     direct = direction_cipher()
#     language = select_language()
#     step = step_direction()
#     answer = []
#     if language == 'рус':
#         lang_abc_up = rus_al_up
#         lang_abc_low = rus_al_low
#     else:
#         lang_abc_up = en_al_up
#         lang_abc_low = en_al_low
#     if direct == '+':
#         ciphr_abc_up = lang_abc_up[step:] + lang_abc_up[:step]
#         ciphr_abc_low = lang_abc_low[step:] + lang_abc_low[:step]
#     else:
#         ciphr_abc_up = lang_abc_up[-step:] + lang_abc_up[:-step]
#         ciphr_abc_low = lang_abc_low[-step:] + lang_abc_low[:-step]
#     for i in range(len(text)):
#         if text[i].isalpha():
#             if text[i].isupper():
#                 symbol_index = lang_abc_up.index(text[i])
#                 answer += ciphr_abc_up[symbol_index]
#             elif text[i].islower():
#                 symbol_index = lang_abc_low.index(text[i])
#                 answer += ciphr_abc_low[symbol_index]
#         else:
#             answer += text[i]
#     return ''.join(answer)


# print(caesar_ciphr())

# def step_direction(text):
#     steps = []
#     text = [i for i in text if i not in '!#$%&*+-=?@^_.,";:']
#     text = ''.join(text)
#     text = text.split()
#     for j in range(len(text)):
#         steps.append(len(text[j]))
#     return steps

# def caesar_ciphr():
#     text = input()
#     steps = step_direction(text)
#     answer = []
#     j = 0
#     k = 0
#     for i in range(len(text)):
#         ciphr_abc_up = en_al_up[steps[j]:] + en_al_up[:steps[j]]
#         ciphr_abc_low = en_al_low[steps[j]:] + en_al_low[:steps[j]]
#         if text[i].isalpha():
#             if text[i].isupper():
#                 symbol_index = en_al_up.index(text[i])
#                 answer += ciphr_abc_up[symbol_index]
#                 k += 1
#             elif text[i].islower():
#                 symbol_index = en_al_low.index(text[i])
#                 answer += ciphr_abc_low[symbol_index]
#                 k += 1
#         else:
#             answer += text[i]
#         if steps[j:] != steps[-1:]:
#             if k == steps[j]:
#                 j += 1
#                 k = 0
#     return ''.join(answer)

# print(caesar_ciphr())

# def perevod(num, system):
#     summ = 0
#     digits = [10, 11, 12, 13, 14, 15]
#     abcd = ['a', 'b', 'c', 'd', 'e', 'f']
#     for i in range(len(num)):
#         bob = num[i]
#         if bob in abcd:
#             bob = digits[abcd.index(bob)]
#         summ += int(bob) * (system ** (len(num) - 1 - i))
#     return summ

# num = input().lower()
# system = int(input())
# print(perevod(num, system))


# def perevod(num, system):
#     summ = []
#     digits = [10, 11, 12, 13, 14, 15]
#     abcd = ['a', 'b', 'c', 'd', 'e', 'f']
#     last = ''
#     total = []
#     while num >= system:
#         summ.append(str(num % system))
#         num //= system
#         last = str(num)
#     if int(last) in digits:
#         last = abcd[digits.index(last)].upper()
#     for i in range(len(summ)):
#         if int(summ[i]) in digits:
#             summ[i] = str(abcd[digits.index(int(summ[i]))].upper())
#     total.append(last)
#     total.extend(summ[::-1])
#     total = ''.join(total)
#     if total.isdigit():
#         total = int(total)
#     return total

# num, system = int(input()), int(input())
# print(perevod(num, system))

# def perevod(num):
#     binary = bin(num)
#     octal = oct(num)
#     _hex = hex(num).upper()
#     return binary[2:], octal[2:], _hex[2:]

# print(*perevod(int(input())), sep='\n')


### GAME_GUESS_WORD ###
word_list = ['виселица', 'дракон', 'человек', 'пакет', 'сколопендра', 
'парашют', 'сом', 'вася', 'соня', 'маракуйя', 'крепость', 'кинофильм', 
'путник', 'кожура', 'перекресток', 'аорта', 'сокол', 'рефрежератор', 
'мор', 'бобер', 'бригада', 'паста', 'кружка', 'жираф', 'лист']
rus_al_up = [chr(ord('А') + i) for i in range(32) if chr(ord('А') + i) != 'Ё']
rus_al_low = [chr(ord('а') + i) for i in range(32) if chr(ord('А') + i) != 'ё']

def get_word():
    word = random.choice(word_list).upper()
    return word

def display_hangman(tries):
    stages = [
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def is_true(letter, guessed_words, guessed_letters):
    if not letter.isalpha():
        print('Вы ввели символ, неявляющийся буквой. Попыта не засчитана, попробуйте еще раз.')
        return True
    if 1 < len(letter) < len(word):
        print('Вы ввели болше одной буквы и не ввели слово целиком, думаю это ошибка, попробуйте еще раз.')
        return True
    if letter in guessed_letters:
        print('Вы вводили эту букву, попробуйте еще раз.')
        return True
    if letter in guessed_words:
        print('Вы вводили это слово, попробуйте еще раз.')
        return True
    if len(letter) == 1:
        if letter not in rus_al_up and letter not in rus_al_low:
            print('Буква чужого алфавита или буква "Ё". Попробуйте еще раз.')
            return True

def play_game(word):
    word_completion = ['_'] * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    answer = ''
    t = 0
    print('Давай сыграем в игру.', display_hangman(tries), word_completion, sep='\n')
    print()
    while True:
        letter = input('Введите предполагаемое слово или букву: ').upper()
        t += 1
        if is_true(letter, guessed_words, guessed_letters):
            continue
        if letter not in word:
            tries -= 1
            if len(letter) == 1:
                guessed_letters.append(letter)
                print('Неверно, эта буква не подходит.')
            else:
                guessed_words.append(letter)
                print('Неверно, это слово не подходит.')
            print(display_hangman(tries), word_completion, sep='\n')

        if tries == 0:
            print(f'К сожалению, вы проиграли, вам конец. Загадано было слово: {word}.')
            break
        if letter in word:
            guessed_letters.append(letter)
            for i in range(len(word)):
                if letter == word[i]:
                    word_completion[i] = word[i]
                    answer = ''.join(word_completion)
            print(display_hangman(tries), word_completion, sep='\n')
            if letter == word or answer.upper() == word:
                print(f'Все верно, вы угадали слово "{word}" и победили в этой игре!', f'Всего попыток = {t}', sep='\n')
                if guessed_words != []:
                    print(f'Попытки введения слов: {guessed_words}')
                if guessed_letters != []:
                    print(f'Попытки введения букв: {guessed_letters}')
                break
            continue

word = get_word()
play_game(word)

# КОНЕЦ КУРСА