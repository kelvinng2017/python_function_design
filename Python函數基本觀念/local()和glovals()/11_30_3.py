"""
列出所有區域變數與全域的内容
"""


def printlocal():
    lang = "Java"
    print("語言: ", lang)
    print("區域變數: ", locals())


msg = "Python"
printlocal()
print("語言:", msg)
print("全域變數:", globals())
