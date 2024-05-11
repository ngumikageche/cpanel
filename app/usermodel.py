from sqlalchemy import Table, Text, Float, Enum, DateTime
from datetime import datetime
import pytz

# Association tables:
user_products = Table('user_products', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    comp_email = db.Column(db.String(120), unique=True, nullable=False)
    products = db.relationship('Product', secondary=user_products, backref=db.backref('users', lazy='dynamic'))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(Text, nullable=False)
    description = db.Column(Text, nullable=True)
    price = db.Column(Float, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    image = db.Column(Text, nullable=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(Text, nullable=False)
    products = db.relationship('Product', backref='category')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(Enum('pending', 'shipped', 'delivered'))
    products = db.relationship('Product', secondary=order_products)
    order_date = db.Column(DateTime, default=datetime.now(pytz.timezone('Africa/Nairobi')))

order_products = Table('order_products', db.Model.metadata,
    db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
)
