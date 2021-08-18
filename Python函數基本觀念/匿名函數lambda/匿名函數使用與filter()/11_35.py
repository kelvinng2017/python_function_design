"""
11_35.py重新設計11_34.py將filter object轉為串列
"""


def oddfn(x):
    return x if(x % 2 == 1) else None


mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)  # 傳回filter object
oddlist = [item for item in filter_object]
# 輸出奇數串列
print("奇數串列: ", oddlist)
