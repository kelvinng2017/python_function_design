"""
11_37.py:使用匿名函數對串列元素執行計算平方運輸
"""
mylist = [5, 10, 15, 20, 25, 30]

squarelist = list(map(lambda x: x**2, mylist))

# 輸出串列元素的平方值

print("串列的平方值: ", squarelist)
