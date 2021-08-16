"""
11_24.py：從新設計11_23.py傳遞參數時第一個參數是冰淇淋的種類，然後才是不同數量的冰淇淋的配料

"""


def make_icream(icecream_type, *toppings):
    # 列出製作冰淇淋的配料
    print("這個 ", icecream_type, "冰淇淋所加的配料如下")
    for topping in toppings:
        print("--- ", topping)


make_icream('香草', '草莓醬')
make_icream('芒果', '草莓醬', '葡萄乾', '巧克力碎片')
