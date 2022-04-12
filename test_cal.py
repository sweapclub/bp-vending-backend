import math
import time
wallet = {
    '1': 100,
    "5": 200,
    "10": 100,
    '20': 40,
    "50" : 10,
    "100" : 20,
    "500": 3,
    "1000" : 2
}
wallet = {
    '1': 100,
    "5": 200,
    "10": 100,
    '20': 40,
    "50" : 10,
    "100" : 20,
    "500": 3,
    "1000" : 2
}

# check if all price is larger than exit

# end

def profile(f):
    is_evaluating = False
    def g(x):
        nonlocal is_evaluating
        if is_evaluating:
            return f(x)
        else:
            start_time = time.time()
            is_evaluating = True
            try:
                value = f(x)
            finally:
                is_evaluating = False
            end_time = time.time()
            print('time taken: {time}'.format(time=end_time-start_time))
            return value
    return g

# 1. when price cant return ! insert 1 10 coin but price is 3 baht


def ton_tung(change):
    ts = time.time()
    change_detail = []
    change, used = cal_change(10, change)
    if used != 0:
        change_detail.append({"toc": '10', "amount": used})
    change, used = cal_change(5, change)
    if used != 0:
        change_detail.append({"toc": '5', "amount": used})
    change, used = cal_change(1, change)
    if used != 0:
        change_detail.append({"toc": '1', "amount": used})

    print(change_detail)
    print('cant change ! {} baht'.format(change))
    te = time.time()
    print(' %2.22f ms' % ( (te - ts) * 1000))


def cal_change(value, change):
    used = 0
    if (wallet[str(value)] != 0):
        value_left = wallet[str(value)] * value
        if(value_left > change):
            used = math.floor(change / value)
            wallet[str(value)] = wallet[str(value)] - used
            change = change % value
        else:
            change = change - value_left
            used = wallet[str(value)]
            wallet[str(value)] = 0

    return change, used



#  recursive type
def cal_recursive(coin_left, value, change, used=0):
    print(change < value,coin_left == 0)
    if (coin_left == 0 or change < value):
        return change, used
    else:
        coin_left = coin_left - 1
        change = change - value
        used = used + 1
        return cal_recursive(coin_left,value, change, used)

def cal(change):
    change, used = cal_recursive(wallet['10'], 10, change)
    change, used = cal_recursive(wallet['5'], 5, change)
    change, used = cal_recursive(wallet['1'], 1, change)
    print(change, used)


x = profile(cal)
print(x(5))

# z = profile(ton_tung)
# print(z(2735))
