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
    role = Column(String, default="admin", nullable=False)

    orders = relationship("Order", back_populates="user")

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    products = relationship("Product", back_populates="admin")    

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    admin_id = Column(Integer, ForeignKey("admins.id"), nullable=False)

    admin = relationship("Admin", back_populates="products")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    user = relationship("User", back_populates="orders")
    product = relationship("Product")
