import datetime

from sqlalchemy import Column, Integer, String, Float, Text, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


__all__ = [
    "SuperAdmin", "Market", "Categories", "Firm", "Base",
    "Products", "User", "DescriptionSeller", "DescriptionCostumer"
    ]


class SuperAdmin(Base):
    """ Пароли/Названия не должны превышать 32 символов (сообщить!)"""
    __tablename__ = "super_admin"

    id = Column(Integer, primary_key=True)      # можно ли в id'шку прокинуть id из ТГ?
    id_telegram = Column(Integer, unique=True)
    password = Column(String(32))



market_users_association_table = Table("market_users_table", Base.metadata,
                                       Column("market_id", ForeignKey("market_table.id"), primary_key=True),
                                       Column("user_id", ForeignKey("user_table.id"), primary_key=True)
                                       )


class Market(Base):
    __tablename__ = "market_table"

    id = Column(Integer, primary_key=True)
    admin_id = Column(Integer)
    title = Column(String(32))
    rating = Column(Float)
    location = Column(String(32))
    description = Column(Text)
    subscription = Column(Boolean, default=True)
    datetime_subscription = Column(DateTime)    # Уточнить про Datetime
    datetime_registration = Column(DateTime, default=datetime.datetime.utcnow)

    users_costumers = relationship("User", secondary=market_users_association_table,
                                   back_populates="markets"
                                   )

    categories = relationship("Categories", back_populates="market")


class Categories(Base):
    __tablename__ = "categories_table"

    id = Column(Integer, primary_key=True)
    category = Column(String(32))

    market_id = Column(Integer, ForeignKey("market_table.id"))
    market = relationship("Market", back_populates="categories")

    firms = relationship("Firm", back_populates="categories")


class Firm(Base):
    __tablename__ = "firm_table"

    id = Column(Integer, primary_key=True)
    title = Column(String(32))

    category_id = Column(Integer, ForeignKey("categories_table.id"))
    categories = relationship("Categories", back_populates="firms")

    products = relationship("Products", back_populates="firm")


class Products(Base):
    __tablename__ = "product_table"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    firm_id = Column(Integer, ForeignKey("firm_table.id"))
    firm = relationship("Firm", back_populates="products")


class User(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    id_telegram = Column(Integer, unique=True)
    like = Column(Integer, default=0)
    dislike = Column(Integer, default=0)
    markets = relationship("Market", secondary=market_users_association_table,
                           back_populates="users_costumers")


class DescriptionSeller(Base):
    __tablename__ = "description_seller"

    id = Column(Integer, primary_key=True)
    about_seller = Column(Text)
    instruction_seller = Column(Text)
    regulations_seller = Column(Text)
    acquainted_seller = Column(String(16))


class DescriptionCostumer(Base):
    __tablename__ = "description_costumer"

    id = Column(Integer, primary_key=True)
    about_costumer = Column(Text)
    instruction_costumer = Column(Text)
    regulations_costumer = Column(Text)
    acquainted_costumer = Column(String(16))
