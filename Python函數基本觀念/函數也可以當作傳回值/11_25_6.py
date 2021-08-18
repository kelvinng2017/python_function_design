"""
這是計算1-(n-1)的總和，觀察函數當作傳回值的應用，這個程式的第6-11行是outer()函數，第11行的傳回值是不含()的inner。
"""


def outer():
    def inner(n):
        print('inner running')
        print("n=%d" % n)
        return sum(range(n))  # range(5)=0+1+2+3+4=10
    return inner


f = outer()  # outer()傳回inner地址
print(f)  # 列印inner記憶體
print(f(5))  # 實際執行的inner()

y = outer()
print(y)
print(y(10))
