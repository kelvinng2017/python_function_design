"""
匿名函數最大特色是可以有許多的參數，但是只有一個程式碼表達式，然後可以執行結果回傳。
lambda arg1[,arg2,...argn]:expression #arg1是參數，可以有多個參數
上述expression就是匿名函數lambda表達式的内容
11_31.py使用一般函數設計傳回平方值
"""
# 使用一般函數


def square(x):
    value = x**2
    return value


# 輸出平方值
print(square(10))
