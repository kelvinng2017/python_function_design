"""
11_30.py 區域變數在主程式引用產生錯誤的實例。
"""


def defmsg():
    msg = 'prinngmsg variable'


print(msg)  # 主程式列印區域變數產生錯誤

"""
上述程式的錯誤原因主要程式内沒有定義msg變數，所以產生程式錯誤
"""
