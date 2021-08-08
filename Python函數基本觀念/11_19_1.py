# 11_19_1.py:主程式呼叫函數時傳遞整數變數，這個程式會在主程式以及函數中列出此變數的值與位址的變化

def mydata(n):
    print("函 數id(n)=:",id(n),"\t",n)
    n =5 
    print("函 數 id(n)=:",id(n),"\t",n)

x = 1
print("主程式 id(x) = : ",id(x),"\t",x)
mydata(x)
print("主程式 id(x) = : ",id(x),"\t",x)