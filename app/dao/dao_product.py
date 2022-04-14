from app.model.sqlite_schema import Product
from app.model import db


def get_all_product():
    error_message = None
    products = None
    try:
        products = db.query(Product).all()
    except Exception as e:
        print(e)
        error_message = "Error has occurred"
    return products, error_message


def get_product(product_id):
    error_message = None
    product = None
    try:
        product = db.query(Product).filter(
            Product.product_id == product_id).first()
    except Exception as e:
        error_message = "Error has occurred"
    return product, error_message


def update_stock(product_id, update_stock):
    error_message = None
    try:
        updater = db.query(Product).filter(Product.product_id == product_id)
        if updater.count() == 0:
            error_message = "Cant find Product with this id"
        else:
            updater.update(
                {
                    Product.amount: update_stock
                },
                synchronize_session=False,
            )
            db.commit()
    except Exception as e:
        db.rollback()
        error_message = "Error has occurred"
    return error_message
