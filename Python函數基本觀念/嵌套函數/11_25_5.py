"""
11_25_5.py 計算2個座標點之距離，外層函數是第6-11行的dist(),此函數第7-8行是內層mySqrt()函數
"""


def dist(x1, y1, x2, y2):  # 計算2點之距離函數
    def mySqrt(z):  # 計算開根號值
        return z**0.5
    dx = (x1-x2)**2
    dy = (y1-y2)**2
    return mySqrt(dx+dy)


print(dist(0, 0, 1, 1))
