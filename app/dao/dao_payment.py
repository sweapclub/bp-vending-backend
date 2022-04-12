from app.model.sqlite_schema import Wallet
from app.model import db


def get_wallet():
    error_message = None
    products = None
    try:
        products = db.query(Wallet).first()
    except Exception as e:
        print(e)
        error_message = "Error has occurred"
    return products, error_message


def update_wallet(wallet: Wallet):
    error_message = None
    try:
        db.query(Wallet).update(
            {
                Wallet.coin_1: wallet.coin_1,
                Wallet.coin_5: wallet.coin_5,
                Wallet.coin_10: wallet.coin_10,
                Wallet.bank_20: wallet.bank_20,
                Wallet.bank_50: wallet.bank_50,
                Wallet.bank_100: wallet.bank_100,
                Wallet.bank_500: wallet.bank_500,
                Wallet.bank_1000: wallet.bank_1000,
            },
            synchronize_session=False,
        )
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        error_message = "Error has occurred"
    return error_message
