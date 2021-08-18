"""
11_29.py區域變數在其它函數引用，造成程式錯誤的應用。
"""


def defmsg():
    msg = 'pringmsg variables'


def printmsg():
    print(msg)  # 列印defmsg()函數定義的區域變數


printmsg()

"""
上述程式的錯誤原因主要是printmsg()函數内沒有定義msg變數，所以產生程式錯誤
"""
