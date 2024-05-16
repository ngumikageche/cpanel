from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship, backref
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    company_email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    authentication_level = Column(Integer, nullable=False)
    status = Column(Boolean, default=True)
    
    orders = relationship('Order', backref='user')
    user_products = relationship('UserProduct', backref='user')

class Category(db.Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    products = relationship('Product', backref='category')

class Product(db.Model):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    image_url = Column(String, nullable=False)
    
    user_products = relationship('UserProduct', backref='product')
    order_products = relationship('OrderProduct', backref='product')

class Order(db.Model):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(String, nullable=False)
    order_date = Column(DateTime, nullable=False)
    
    order_products = relationship('OrderProduct', backref='order')

class UserProduct(db.Model):
    __tablename__ = 'user_products'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

class OrderProduct(db.Model):
    __tablename__ = 'order_products'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
