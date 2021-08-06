# argument_value_none.py
def greeting(name):
    """Python函數需要傳遞名字name"""
    print("Hi", name, "Good Morning")


ret_value = greeting('Nelson')
print("greeting()值回傳=", ret_value)
print(ret_value, "的 type = ", type(ret_value))
