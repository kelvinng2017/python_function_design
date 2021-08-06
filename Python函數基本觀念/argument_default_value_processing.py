# argument_default_value_processing.py


def interest(interest_type, subject="敦煌"):
    """顯示與興趣和主題"""
    print("我的興趣是" + interest_type)
    print("在 "+interest_type + "中，最喜歡的是 " + subject)
    print()


interest('旅遊')  # 傳遞一個參數
interest(interest_type='旅遊')  # 傳遞一個參數
interest('旅遊', '張家界')
interest(interest_type='旅遊', subject='張家界')
interest(subject='張家界', interest_type='旅遊')
interest('閱讀', '旅遊類')
