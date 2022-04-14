from app.dto.dto_common import OutputStatus
from fastapi import APIRouter
from app.dao.dao_payment import (get_wallet, update_wallet)
from app.dao.dao_product import (get_product, update_stock)
from app.dao.dao_report import (add_to_report)

from app.dto.dto_payment import (
    OutputGetWallet, OutputPayment, Wallet, InputPayment, ChangeDetail)
router = APIRouter(
    prefix="/payments",
    tags=["Payments"],
    responses={404: {"description": "Not found"}}
)


@router.patch('/', summary="Adjust money in machine", response_model=OutputStatus)
async def patch_update_wallet(wallet: Wallet):
    error_message = update_wallet(Wallet(
        coin_1=wallet.coin_1,
        coin_5=wallet.coin_5,
        coin_10=wallet.coin_10,
        bank_20=wallet.bank_20,
        bank_50=wallet.bank_50,
        bank_100=wallet.bank_100,
        bank_500=wallet.bank_500,
        bank_1000=wallet.bank_1000,
    ))

    if error_message != None:
        return OutputPayment(status="Fail", errorMessage=error_message)
    return OutputStatus(status="Success")


@router.post('/', summary="Payment and change methods", response_model=OutputPayment)
async def post_payment(input: InputPayment):

    product, error_message = get_product(input.productId)
    if error_message != None:
        return OutputPayment(status="Fail", errorMessage=error_message)
    elif product == None:
        return OutputPayment(status="Fail", errorMessage="Dont have this product in Vending machine")
    elif product.amount < input.amount:
        return OutputPayment(status="Fail", errorMessage="Amount is greater than in-stock")

    money = input.money
    total_price = product.price * input.amount
    change = money - total_price
    # print(money, total_price, change)

    if change < 0:
        return OutputPayment(status="Fail", errorMessage="Your money is not enough...")

    db_wallet, error_message = get_wallet()
    if error_message != None:
        return OutputPayment(status="Fail", errorMessage=error_message)

    wallet = db_wallet.__dict__
    combine_wallet_with_income(db_wallet.__dict__, input.moneyDetail)
    wallet, change_log, change_left = calculate_change(wallet, change)

    # add just wallet

    if error_message != None:
        return OutputPayment(status="Fail", errorMessage=error_message)

    if change_left != 0:
        #  suggestion !!
        suggestion = []
        if (change < 10):
            suggestion.append(
                'Decrese money to {} baht'.format(money - change_left))
            if (wallet['coin_5'] >= 1):
                suggestion.append(
                    'Increse money to {} baht'.format(money + (5 - (change_left % 5))))

        print(suggestion)
        return OutputPayment(status="Fail", suggestion=suggestion, errorMessage="We dont have enough change...".format(money - change_left))
    else:
        error_message = update_wallet(Wallet(
            coin_1=wallet['coin_1'],
            coin_5=wallet['coin_5'],
            coin_10=wallet['coin_10'],
            bank_20=wallet['bank_20'],
            bank_50=wallet['bank_50'],
            bank_100=wallet['bank_100'],
            bank_500=wallet['bank_500'],
            bank_1000=wallet['bank_1000'],
        ))

        if error_message != None:
            return OutputPayment(status="Fail", errorMessage=error_message)

        error_message = update_stock(
            input.productId, product.amount - input.amount)
        if error_message != None:
            return OutputPayment(status="Fail", errorMessage=error_message)
        error_message = add_to_report(product_name=product.product_name, product_price=product.price,
                                      amount=input.amount, input_money=money, change=change)
        if error_message != None:
            print(error_message)
        change_detail = []
        for c in change_log:
            if (c['amount'] > 0):
                change_detail.append(ChangeDetail(
                    toc=c['toc'], amount=c['amount']))
        return OutputPayment(status="Success", data=change_detail)


@router.get('/', summary="Current Money", response_model=OutputGetWallet)
async def get_current_money():
    wallet, error_message = get_wallet()
    if error_message != None:
        return OutputGetWallet(status="Fail", errorMessage=error_message)
    result = Wallet(
        coin_1=wallet.coin_1,
        coin_5=wallet.coin_5,
        coin_10=wallet.coin_10,
        bank_20=wallet.bank_20,
        bank_50=wallet.bank_50,
        bank_100=wallet.bank_100,
        bank_500=wallet.bank_500,
        bank_1000=wallet.bank_1000,
    )
    return OutputGetWallet(status="Success", data=result)

# helper


def cal_recursive(amount, value, change, used=0):
    if (amount == 0 or change < value):
        return change, used
    else:
        amount = amount - 1
        change = change - value
        used = used + 1
        return cal_recursive(amount, value, change, used)


def calculate_change(wallet: Wallet, change):
    change_detail = []
    # change, used = cal_recursive(wallet.bank_1000, 1000, change)
    # wallet.bank_1000 -= used
    # change_detail.append({"toc": '1000', "amount": used})
    # change, used = cal_recursive(wallet.bank_500, 500, change)
    # wallet.bank_500 -= used
    # change_detail.append({"toc": '500', "amount": used})
    # change, used = cal_recursive(wallet.bank_100, 100, change)
    # wallet.bank_100 -= used
    # change_detail.append({"toc": '100', "amount": used})
    # change, used = cal_recursive(wallet.bank_50, 50, change)
    # wallet.bank_50 -= used
    # change_detail.append({"toc": '50', "amount": used})
    # change, used = cal_recursive(wallet.bank_20, 20, change)
    # wallet.bank_20 -= used
    # change_detail.append({"toc": '20', "amount": used})
    # change, used = cal_recursive(wallet.coin_10, 10, change)
    # wallet.coin_10 -= used
    # change_detail.append({"toc": '10', "amount": used})
    # change, used = cal_recursive(wallet.coin_5, 5, change)
    # wallet.coin_5 -= used
    # change_detail.append({"toc": '5', "amount": used})
    # change, used = cal_recursive(wallet.coin_1, 1, change)
    # wallet.coin_1 -= used
    # change_detail.append({"toc": '1', "amount": used})
    change, used = cal_recursive(wallet['bank_1000'], 1000, change)
    wallet['bank_1000'] -= used
    change_detail.append({"toc": '1000', "amount": used})
    change, used = cal_recursive(wallet['bank_500'], 500, change)
    wallet['bank_500'] -= used
    change_detail.append({"toc": '500', "amount": used})
    change, used = cal_recursive(wallet['bank_100'], 100, change)
    wallet['bank_100'] -= used
    change_detail.append({"toc": '100', "amount": used})
    change, used = cal_recursive(wallet['bank_50'], 50, change)
    wallet['bank_50'] -= used
    change_detail.append({"toc": '50', "amount": used})
    change, used = cal_recursive(wallet['bank_20'], 20, change)
    wallet['bank_20'] -= used
    change_detail.append({"toc": '20', "amount": used})
    change, used = cal_recursive(wallet['coin_10'], 10, change)
    wallet['coin_10'] -= used
    change_detail.append({"toc": '10', "amount": used})
    change, used = cal_recursive(wallet['coin_5'], 5, change)
    wallet['coin_5'] -= used
    change_detail.append({"toc": '5', "amount": used})
    change, used = cal_recursive(wallet['coin_1'], 1, change)
    wallet['coin_1'] -= used
    change_detail.append({"toc": '1', "amount": used})
    return wallet, change_detail, change


def combine_wallet_with_income(vending, customer):
    vending['coin_1'] += customer.coin_1
    vending['coin_5'] += customer.coin_5
    vending['coin_10'] += customer.coin_10
    vending['bank_20'] += customer.bank_20
    vending['bank_50'] += customer.bank_50
    vending['bank_100'] += customer.bank_100
    vending['bank_500'] += customer.bank_500
    vending['bank_1000'] += customer.bank_1000

    # return Wallet()
    return vending
