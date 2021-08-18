"""
內部函數是一個動態產生的程式，當它可以記住函數以外的程式所建立的環境變數時，我們可以成稱這個內部函數是閉包(closure)

11_25_7.py:一個線性函數ax+b的閉包說明。
"""


def outer():
    b = 10  # inner所使用的變數值

    def inner(x):
        return 5*x+b  # 引用第3行的b
    return inner


b = 2
f = outer()
print(f)
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(b))
