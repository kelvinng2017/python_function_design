"""
一般在主程式内建立的變數稱爲全域變數，這個變數可以提供主程式内與本程式的所有函數有所引用
11_27.py這個程式
"""


def printmsg():
    # 函數本身沒有定義變數，只有執行列印全域變數功能
    print("函數列印: ", msg)  # 列印全域變數


msg = 'Global Variable'
print("主程式列印: ", msg)
printmsg()
