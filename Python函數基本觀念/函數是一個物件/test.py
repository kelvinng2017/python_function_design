def upperStr(text):
    return text.upper()


print(upperStr('deepstone'))

"""
我們可以使用物件賦值方式處理物件，或是將函數設定給一個變數。
"""

upperLetter = upperStr

print(upperLetter('deepstone'))
"""
函數若是拿掉小括號()，這個函數就是一個記憶體的位址
"""
print(upperStr)
print(upperLetter)

"""
使用type()觀察，可以得到upperStr和upperLetter皆是物件。
"""
print(type(upperStr))
print(type(upperLetter))
