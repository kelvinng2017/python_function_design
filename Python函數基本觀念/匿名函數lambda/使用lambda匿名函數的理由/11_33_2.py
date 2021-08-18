"""
11_33_2.py重新設計ch11_33_1.py，使用一個函數但是有2個方程式。
"""


def func(b):
    return lambda x: 2*x+b


linear = func(5)  # 5將傳給lambda的b
print(linear(10))  # 10是lambda的x

linear2 = func(3)
print(linear2(10))
