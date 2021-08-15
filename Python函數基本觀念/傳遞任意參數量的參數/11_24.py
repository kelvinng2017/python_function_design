"""
11_23.py:建立一個冰淇淋的配料程式，一般冰淇淋可以在上面加上配料，這個程式在呼叫製作冰淇淋函數
make_icecream()時，可以傳遞0到多個配料，然後make_icecream()函數會將配料結果的冰淇淋列出來。
"""


def make_icream(*toppings):  # 加上""*"符號的參數代表可以用0至多個參數將傳遞到這個函數內。
    # 列出製作冰淇淋的配料
    print("這個冰淇淋所加的配料如下")
    for topping in toppings:
        print("---", topping)


make_icream('草莓醬')
make_icream('草莓醬', '葡萄乾', '巧克力碎片')
