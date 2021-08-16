"""
#11_25.py 這個程式基本上是用build_dict()函數建立一個球員的字典資料，
主程式會傳入一般參數與任意數量的關鍵字參數，最後可以列出執行結果。
"""


def build_dict(name, age, **players):
    # 建立NBA球員的字典資料
    info = {}  # 建立空的字典
    info['Name'] = name
    info['Age'] = age
    for key, values in players.items():
        info[key] = values
    return info  # 回傳所建的字典


player_dict = build_dict('James', '32',
                         City='Cleveland',
                         State='Ohio')

print(player_dict)
