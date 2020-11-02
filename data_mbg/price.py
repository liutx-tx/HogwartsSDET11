
import pandas as pd

def caseTest():
    new_price = {}
    old_price = {}
    dif = []

    res1 = pd.read_excel('pr.xlsx',sheet_name='价格调整')
    res2 = pd.read_excel('data2.xlsx', sheet_name='0')
    for code,price in zip(res1['code'],res1['old_price']):
        new_price[code] = str(price)
    for code,price in zip(res2['code'],res2['new_price']):
        old_price[code] = str(price)

    # print(new_price)
    # print(old_price)
    for key,val in new_price.items():
        old_val = old_price.get(key)
        if val == old_val:
            pass
        else:
            dif.append({'code':key,'new_price':val,'old_price':old_val})

    for i in dif:
        print(i)

caseTest()