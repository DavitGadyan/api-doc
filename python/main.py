#coding=utf-8
"""
author:kidd
"""

# python 3.6

from restful import UbiexSDK

def main():
    sdk = UbiexSDK("ed562b4e-6d07-4559-b6c2-26b265d4e12b", "b10bce046efcd6b9afaae5c828d2707f1763509a")
    r = sdk.getFunds(2)
    # print(type(r))
    print("r['data']['usdt']>>>", r['data']['usdt'])

    # print(sdk.getAccounts())


    # r = sdk.transfer(_from=1, to=2, amount=10, coin='usdt', safePwd='david777')

    # print(r)

    # r = sdk.getFunds(2)
    # # print(type(r))
    # print("r['data']['usdt']>>>", r['data']['usdt'])

    # print("balance: ", sdk.getFunds())
    # pr = 47430.69
    # am = 1/pr
    # print(am)
    # r = sdk.order(market='btc_usdt', price=pr, number=am, type=1, entrustType=0)
    # print(r)
    # print("market config: ", sdk.getMarketConfig())
    # print("funds: ", sdk.getFunds())
    # print("getDepth: ", sdk.getDepth("btc_usdt"))
    r = sdk.getOrder(market='btc_usdt', id=161320877011545) # Status (0, submission not matched, 1, unsettled or partially completed, 2, completed, 3, cancelled, 4,matched but in the settlement)
    print(r)
    r = sdk.getFunds(2)
    # print(type(r))
    print("r['data']['btc']>>>", r['data']['btc'])
if __name__ == '__main__':
    main()
