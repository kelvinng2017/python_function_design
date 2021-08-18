"""
11_33_3.py以一般函數當作函數參數的實例
"""


def mycar(cars, func):
    for car in cars:
        print(func(car))


def wdcar(carbrand):
    return "My dream car is "+carbrand.title()


dreamcars = ['porsche', 'rolls royce', 'maserati']
mycar(dreamcars, wdcar)
