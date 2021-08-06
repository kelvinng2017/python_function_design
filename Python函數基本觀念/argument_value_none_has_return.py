# argument_value_none_has_return.py
def greeting(name):
    """Python函數需要傳遞名字name"""
    print("Hi", name, "Good Morning")
    return


ret_value = greeting('Nelson')
print("greeting()值回傳=", ret_value)
print(ret_value, "的 type = ", type(ret_value))
