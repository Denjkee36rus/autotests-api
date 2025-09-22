"""
Напиши функцию, которая принимает список чисел и возвращает их сумму. Нельзя пользоваться встроенной функцией сумм.
"""

# def my_sum(numbers: list):
#     total = 0
#     for num in numbers:
#         if num % 2 == 0:
#            total += num
#     return total

def fibonacchi(n):
    if n < 0:
        raise ValueError("должно быть положительным")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b  = b, a + b
    return b

print(fibonacchi(1))


import functools

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f" name: {func.__name__}")
        print(f"args: {args}")
        print(f"kwargs, {kwargs}")

        return func(*args, **kwargs)
    return wrapper

@log_call
def add(a,b):
    return a + b


