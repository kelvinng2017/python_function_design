"""
重新設計1123.py，驗證"toppings"參數的資料形態是元組。
"""


def make_icecream(*toppings):
    """列出製作冰淇淋的配料"""
    print("這個冰淇淋所加的配料如下")
    for topping in toppings:
        print("---", topping)
    print(type(toppings))
    print(topping)


make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄桿', '巧克力脆皮')
