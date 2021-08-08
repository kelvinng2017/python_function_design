#11_19:傳遞串列給product_msg()函數，函數會遍歷串列，然後列出一封產品發表會的信件。
def product_msg(customers):
    str1 = '親愛的'
    str2 = '本公司將在2020年12月20日北京舉行產品發表會'
    str3 = '總經理:深石敬上'
    for customer in customers:
        msg = str1 + customer + '\n' +str2 +'\n'+str3
        print(msg,'\n')

members = ['Damon','Peter','Mary']
product_msg(members)