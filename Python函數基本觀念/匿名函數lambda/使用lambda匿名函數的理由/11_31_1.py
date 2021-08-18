"""
這是一個2x+b方程式，有2個變數，第5行定義linear時
才確定lambda方程式2x+5，所以第6行可以得到25。
"""

# ch11_33_1.py


def func(b):
    return lambda x: 2*x+b


linear = func(5)  # 5將傳給lambda的b
print(linear(10))
