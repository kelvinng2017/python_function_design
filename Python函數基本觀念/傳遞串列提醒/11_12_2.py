"""
11_22_2.py:將串類參數預設值設為None，重新設計11_22_1.py
"""


def insertChar(letter, myList=None):
    if myList == None:
        print("我在這裡")
        myList = []
    myList.append(letter)
    print(myList)


insertChar('x')
insertChar('y')
