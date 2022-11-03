import math

def sum_digits(a, b):
    return a + b

def diff_digits(a, b):
    return a - b

def product_digis(a, b):
    return a * b

def division_digits(a, b):
    return a / b

def integer_digits(a, b):
    return a // b

def mod_digits(a, b):
    return a % b

def formula_digits(a, b):
    return math.sqrt(a ** 10 + b ** 10)

def list_formula():
    a = int(input())
    b = int(input())
    print(sum_digits(a, b),
    diff_digits(a, b),
    product_digis(a, b),
    division_digits(a, b),
    integer_digits(a, b),
    mod_digits(a, b),
    formula_digits(a, b),
    sep='\n')

list_formula()