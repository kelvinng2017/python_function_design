"""
如果全域變數在函數内可能更改内容時，需要在函數内使用global宣告這個全域變數，程式才不會有錯誤
"""


def printmsg():
    global msg
    msg = "Java"  # 更改全域變數
    print("函數列印:更改後", msg)


msg = "Python"
print("主程式列印:更改前:", msg)
printmsg()
print("主程式列印:更改後:", msg)
