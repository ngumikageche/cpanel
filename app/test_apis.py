import os
import unittest
from io import BytesIO
from flask import current_app
from app import create_app, db
from models.usermodel import Product  # Import your Product model

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = create_app()  # Assuming you have a 'testing' config
        self.client = self.app.test_client()
        
        # Set up the application context
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Create the database and the database table
        db.create_all()

    def tearDown(self):
        # Remove the database session and drop all tables
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_product(self):
        # Simulate form data for the product
        data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': '9.99',
            'stock': '100',
            'category_id': '1',
        }
        
        # Simulate a file upload
        data['image'] = (BytesIO(b'my file contents'), 'test_image.jpg')
        
        # Send a POST request to the /product/create route
        response = self.client.post('/products/product/create', data=data, content_type='multipart/form-data')

        # Check the response status code and data
        self.assertEqual(response.status_code, 201)
        json_data = response.get_json()
        self.assertIn('Product created successfully', json_data['message'])

        # Check that the product was created in the database
        product = Product.query.filter_by(name='Test Product').first()
        self.assertIsNotNone(product)
        self.assertEqual(product.description, 'This is a test product.')
        self.assertEqual(product.price, 9.99)  # Assuming price is stored as a float
        self.assertEqual(product.stock, 100)
        self.assertEqual(product.category_id, 1)
        self.assertEqual(product.image, 'test_image.jpg')

if __name__ == '__main__':
    unittest.main()
