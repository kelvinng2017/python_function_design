"""
11_30_1.py 在函數内嘗試更改全域變數，結果是增加定義一個區域變數
"""


def printmsg():
    msg = "Java"  # 嘗試更改全域變數造成造成建立一個區域變數
    print("更改後:", msg)


msg = "Python"
printmsg()
