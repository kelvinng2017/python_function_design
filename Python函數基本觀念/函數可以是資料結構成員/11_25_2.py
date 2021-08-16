"""
11_25_2.py: 用for迴圈迭代串列內的元素，這些元素是函數，這次有傳遞參數(1,5,10)
"""


def total(data):
    return sum(data)


x = (1, 5, 10)
myList = [min, max, sum, total]
for f in myList:
    print(f, f(x))
