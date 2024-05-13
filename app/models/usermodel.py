from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Float, Text
from sqlalchemy.orm import relationship
from datetime import datetime
import pytz
from app import db
class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    company_email = Column(String(120), unique=True, nullable=False)
    orders = relationship('Order', backref='user')
    products = relationship('Product', secondary='user_product', backref='users')

class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    image_url = Column(Text, nullable=True)
    category = relationship('Category', backref='products')

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    products = relationship('Product', backref='category')

class Order(db.Model):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    status = Column(Enum('pending', 'shipped', 'delivered'), nullable=False, default='pending')
    products = relationship('Product', secondary='order_product')
    order_date = Column(DateTime, default=datetime.now(pytz.timezone('Africa/Nairobi')))

class UserProduct(db.Model):
    __tablename__ = 'user_product'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    product_id = Column(Integer, ForeignKey('product.id'))

class OrderProduct(db.Model):
    __tablename__ = 'order_product'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
