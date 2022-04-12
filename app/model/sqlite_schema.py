from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from . import Base


class Product(Base):
    __tablename__ = "product"

    product_id = Column(String, primary_key=True, index=True)
    product_name = Column(String, index=True, nullable=False)
    amount = Column(Integer, index=True, nullable=False)
    price = Column(Integer, index=True, nullable=False)


class Wallet(Base):
    __tablename__ = "wallet"

    wallet_id = Column(String, primary_key=True)
    coin_1 = Column(Integer, nullable=False)
    coin_5 = Column(Integer, nullable=False)
    coin_10 = Column(Integer, nullable=False)
    bank_20 = Column(Integer, nullable=False)
    bank_50 = Column(Integer, nullable=False)
    bank_100 = Column(Integer, nullable=False)
    bank_500 = Column(Integer, nullable=False)
    bank_1000 = Column(Integer, nullable=False)
