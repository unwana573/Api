from sqlalchemy import Column, ForeignKey, Integer, String
from api.core.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    user_name = Column(String)
    full_name = Column(String)
    phone_number = Column(String)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user", nullable=False)

    orders = relationship("Order", back_populates="user")
    products = relationship("Product", back_populates="admin")

class TokenBlacklist(Base):
    __tablename__ = "token_blacklist"

    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True, nullable=False)

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    admin_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(String, nullable=True)
    quantity = Column(Integer, nullable=True)
    admin = relationship("User", back_populates="products")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    user = relationship("User", back_populates="orders")
    product = relationship("Product")
