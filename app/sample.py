from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pytz

from app import db
from models.usermodel import User, Category, Product, Order, UserProduct, OrderProduct

# Create an engine and a session
engine = create_engine('postgresql:///website')  # Replace 'your_database_url' with your actual database URL
Session = sessionmaker(bind=engine)
session = Session()


# Sample data for User
user1 = User(
    username='john_doe',
    company_email='john_doe@example.com',
    password='hashed_password_1',
    authentication_level=1,
    status=True
)

user2 = User(
    username='jane_smith',
    company_email='jane_smith@example.com',
    password='hashed_password_2',
    authentication_level=2,
    status=True
)

# Sample data for Category
category1 = Category(name='Electronics')
category2 = Category(name='Books')

# Sample data for Product
product1 = Product(
    name='Smartphone',
    description='Latest model smartphone with advanced features',
    price=699.99,
    category=category1,
    image_url='http://example.com/smartphone.jpg'
)

product2 = Product(
    name='Laptop',
    description='High performance laptop for gaming and work',
    price=1299.99,
    category=category1,
    image_url='http://example.com/laptop.jpg'
)

product3 = Product(
    name='Novel',
    description='Bestselling fiction novel',
    price=19.99,
    category=category2,
    image_url='http://example.com/novel.jpg'
)

# Sample data for Order
order1 = Order(
    user=user1,
    status='pending',
    order_date=datetime.now(pytz.timezone('Africa/Nairobi'))
)

order2 = Order(
    user=user2,
    status='shipped',
    order_date=datetime.now(pytz.timezone('Africa/Nairobi'))
)

# Sample data for UserProduct
user_product1 = UserProduct(user=user1, product=product1)
user_product2 = UserProduct(user=user2, product=product2)
user_product3 = UserProduct(user=user1, product=product3)

# Sample data for OrderProduct
order_product1 = OrderProduct(order=order1, product=product1)
order_product2 = OrderProduct(order=order1, product=product3)
order_product3 = OrderProduct(order=order2, product=product2)

# Add and commit the sample data
session.add_all([
    user1, user2, category1, category2,
    product1, product2, product3,
    order1, order2,
    user_product1, user_product2, user_product3,
    order_product1, order_product2, order_product3
])

session.commit()

print("Sample data inserted successfully.")
