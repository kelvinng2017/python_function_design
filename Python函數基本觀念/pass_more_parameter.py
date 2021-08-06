# pass_more_parameter.py
def subtract(x1, x2):
    result = x1 - x2
    print(result)  # 輸出減法結果


print("本程式會執行 a -b 的運算")

a = int(input("a = "))
b = int(input("b = "))
print("a - b = ", end=" ")
subtract(a, b)
