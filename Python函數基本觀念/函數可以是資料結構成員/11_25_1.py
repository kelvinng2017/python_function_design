"""
將所定義的函數total與Python內建的函數min()、max()、sum()等，當作是串列的元素，這些元素是函數，這次有傳遞參數(1,5,10)
"""


def total(data):
    return sum(data)


x = (1, 5, 10)
myList = [min, max, sum, total]
for f in myList:
    print(f)
