# 11_19_2.py:主程式呼叫函數時傳遞串列變數，這個程式會在主程式以及函數中列出此串列變數的值與位址的變化
def mydata(n):
    print("函 數 id(n) = : ", id(n), "\t", n)
    n[0] = 5
    print("函 數 id(n) = : ", id(n), "\t", n)


x = [1, 2]
print("主程式 id(x) = :", id(x), "\t", x)
mydata(x)
print("主程式 id(x) = :", id(x), "\t", x)
