"""
11_28.py:區域變數與全域變數定義了相同的變數msg,但是内容不相同，
然後執行列印，就可以發現在函數與主程式所列印
"""


def printmsg():
    # 函數本身有定義變數功能
    msg = 'Local Variable'  # 設定區域變數
    print("函數列印: ", msg)  # 列印區域變數


msg = 'Global Variable'  # 這是全域變數
print("主程式列印 ", msg)  # 列印全域變數
printmsg()
