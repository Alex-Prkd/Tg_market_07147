import datetime

from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class AdminBot(Base):
    """ Пароли/Названия не должны превышать 32 символов (сообщить!)"""
    __tablename__ = "super_admin"

    id_telegram = Column(Integer, unique=True, primary_key=True, nullable=False)
    photo_bot = Column(String)



class Market(Base):
    __tablename__ = "market_table"

    id = Column(Integer, primary_key=True)
    admin_id = Column(Integer)
    title = Column(String(32))
    rating = Column(Float)
    location = Column(String(32))
    description = Column(Text)
    datetime_subscription = Column(DateTime)    # Уточнить про Datetime
    datetime_registration = Column(DateTime, default=datetime.datetime.utcnow)
    
    users_costumers = relationship("User", backref="market_table")

    categories = relationship("Categories", backref="market_table")


class Categories(Base):
    __tablename__ = "categories_table"

    id = Column(Integer, primary_key=True)
    category = Column(String(32))

    market_id = Column(Integer, ForeignKey("market_table.id"))

    firms = relationship("Firm", backref="categories_table")


class Firm(Base):
    __tablename__ = "firm_table"

    id = Column(Integer, primary_key=True)
    title = Column(String(32))

    category_id = Column(Integer, ForeignKey("categories_table.id"))

    products = relationship("Products", backref="firm_table")


class Products(Base):
    __tablename__ = "product_table"

    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    amount_20mg = Column(Integer)
    amount_45mg = Column(Integer)
    price_for_1 = Column(Integer)
    price_for_10 = Column(Integer)
    price_for_25 = Column(Integer)
    price_for_100 = Column(Integer)
    firm_id = Column(Integer, ForeignKey("firm_table.id"))


class User(Base):
    __tablename__ = "user_table"

    id_telegram = Column(Integer, primary_key=True, unique=True, nullable=False)
    username = Column(String(32))
    like = Column(Integer, default=0)
    dislike = Column(Integer, default=0)
    role = Column(String(16), default="costumer")
    blacklist = Column(Boolean, default=0)

    market_id = Column(Integer, ForeignKey("market_table.id"))


class Description(Base):
    __tablename__ = "description_seller"

    id = Column(Integer, primary_key=True)
    about_seller = Column(Text)
    instruction_seller = Column(Text)
    regulations_seller = Column(Text)
    about_costumer = Column(Text)
    instruction_costumer = Column(Text)
    regulations_costumer = Column(Text)


class Blacklist(Base):
    __tablename__ = "blacklist"

    id_telegram = Column(Integer, primary_key=True, unique=True, nullable=False)
    username = Column(String(32))
    role = Column(String(16))

