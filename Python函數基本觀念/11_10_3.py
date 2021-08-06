# 11_10_3.py
def is_None(string, x):
    """顯示"""
    if x is None:
        print("%s = None" % string)
    elif x:
        print("%s = True" % string)
    else:
        print("%s = False" % string)


is_None("空串列", [])
is_None("空元組", ())
is_None("空字典", {})
is_None("空集合", set())
is_None("None ", set())
is_None("True ", True)
is_None("False ", False)
