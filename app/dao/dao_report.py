from app.model.sqlite_schema import Report, Product
from app.model import db
from sqlalchemy.sql import func
from datetime import datetime


def generate_report():
    error_message = None
    result = None
    try:
        result = db.query(Report).all()
    except Exception as e:
        error_message = "Error has occurred"
    return result, error_message


def add_to_report(product_name, product_price, amount, input_money, change):
    error_message = None

    transaction = Report(
        report_ts=datetime.now(), product_name=product_name, product_price=product_price, amount=amount, input_money=input_money, change=change
    )
    try:
        db.add(transaction)
        db.commit()
    except Exception as e:
        db.rollback()
        error_message = "Error has occurred"
    return error_message
