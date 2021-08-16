"""
在呼叫make_icecream()時沒有傳遞的觀察。
"""


def make_icream(*toppings):
    """列出製作冰淇淋的配料"""
    for topping in toppings:
        print("---", topping)


make_icream()
