"""
閉包closure的另外一個應用，這也是線性函數ax+b，不過環境變數是outer()的參數。
"""


def outer(a, b):
    '''a和b將是inner()的環境變數'''
    def inner(x):
        return a * x + b
    return inner


f1 = outer(1, 2)
f2 = outer(3, 4)

print(f1(1), f2(3))
