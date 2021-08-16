"""
11_25_3.py 函數當作是傳遞參數的基本應用
"""


def add(x, y):
    return x+y


def mul(x, y):
    return x*y


def running(func, arg1, arg2):
    return func(arg1, arg2)


result1 = running(add, 5, 10)  # add函數當作參數
print(result1)
result2 = running(mul, 5, 10)  # mul函數當作參數
print(result2)

"""
running()函數可以接受其它函數當作參數的函數又稱此為高階函數(Higher-order function)
"""
