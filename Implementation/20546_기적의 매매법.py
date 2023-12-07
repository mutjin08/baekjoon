def bnp():
    mycash, mystock = cash, 0
    for price in prices:
        if mycash >= price:
            mystock += mycash//price
            mycash %= price
        else:
            continue
    return mycash + prices[-1]*mystock

def timing():
    mycash, mystock = cash, 0
    
    for i in range(3, len(prices)):
        if prices[i]>mycash:
            continue
        
        # 전량 매수
        if prices[i-3] > prices[i-2] > prices[i-1] > prices[i]:
            mystock += mycash//prices[i]
            mycash %= prices[i]
        # 전량 매도
        elif prices[i-3] < prices[i-2] < prices[i-1] < prices[i]:
            mycash += mystock*prices[i]
            mystock = 0
        else:
            continue

    return mycash + prices[-1]*mystock


def solution():
    bnp_res = bnp()
    timing_res = timing()

    if bnp_res > timing_res:
        return "BNP"
    elif timing_res > bnp_res:
        return "TIMING"
    else:
        return "SAMESAME"

cash = int(input())
prices = list(map(int, input().split()))

print(solution())