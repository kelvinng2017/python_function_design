"""
在Python的程式中還提供一種變數稱nonlocal變數，它的用法與global相同，不過global是指最上層變數、nonlocal指的是上一層變數
"""


def local_fun():
    var_nonlocal = 22

    def local_inner():
        global var_global
        nonlocal var_nonlocal
        var_global = 111
        var_nonlocal = 222

    local_inner()
    print('local_fun輸出 var_global = ', var_global)
    print('local_fun輸出 var_nonlocal =', var_nonlocal)


var_global = 1
var_nonlocal = 2

print('主程式輸出 var_global = ', var_global)
print('主程式輸出 var_nonlocal = ', var_nonlocal)

local_fun()
print('主程式輸出 var_gloval = ', var_global)
print('主程式輸出 var_noncal = ', var_nonlocal)
