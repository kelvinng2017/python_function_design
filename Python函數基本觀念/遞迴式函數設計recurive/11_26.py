"""
11_26.py 使用遞迴函數執行階層(factorial)運算
"""


def factorial(n):
    # 計算n的階層，n必須是正數
    print("n%d" % n)
    if n == 1:
        return 1
    else:
        return (n*factorial(n-1))


value = 3
print(value, " 的階層結果是", factorial(value))
value = 5
print(value, " 的階層結果是 ", factorial(value))
