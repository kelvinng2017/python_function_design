"""
11_22_1.py:這個insertChar()函數有2個參數，第一個參數內容可以是任意資料，第二個參數是空串列myList，
程式預期是每次呼叫insertChar()時將第一個參數內容插入第二個空串列內。
"""


def insertChar(letter, myList=[], inList=[1, 2]):
    print(letter)
    myList.append(letter)
    inList.append(letter)
    print(myList)
    print(inList)
    # myList.append(letter)


insertChar('x')
insertChar('y')
