"""
11_37_3.py設計字串轉整數的函數，爲了驗證轉整數正確，筆者將此字串加10，最後再輸出。
"""
from functools import reduce


def strToInt(s):
    def func(x, y):
        return 10*x+y

    def charToNum(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(func, map(charToNum, s))


string = '5487'
x = strToInt(string) + 10

print("x = ",  x)
