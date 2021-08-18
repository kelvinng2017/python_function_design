"""
11_33_4.py:重新設計11_33_3.py，使用匿名函數取代wdcar()
"""


def mycar(cars, func):
    for car in cars:
        print(func(car))


dreamcars = ['porsche', 'rolls royce', 'maserati']
mycar(dreamcars, lambda carbarnd: "My dream car is "+carbarnd.title())
