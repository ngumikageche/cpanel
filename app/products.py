from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # or your actual database URI
app.config['UPLOAD_FOLDER'] = '/path/to/upload/folder'  # replace with your upload folder path
db = SQLAlchemy(app)

# Your User and Product models go here

@app.route('/product/create', methods=['POST'])
def create_product():
    # Get form data
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    image = request.files.get('image')

    # Save the image file
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Create a new product
    product = Product(name=name, description=description, price=price, image=filename)
    db.session.add(product)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/product/<int:id>', methods=['GET'])
def read_product(id):
    product = Product.query.get(id)
    return render_template('product.html', product=product)

@app.route('/product/<int:id>', methods=['POST'])
def update_product(id):
    product = Product.query.get(id)

    # Update product fields
    product.name = request.form.get('name')
    product.description = request.form.get('description')
    product.price = request.form.get('price')

    # Check if a new image was uploaded
    image = request.files.get('image')
    if image:
        # Delete the old image file
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], product.image))

        # Save the new image file
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Update the image field
        product.image = filename

    db.session.commit()

    return redirect(url_for('index'))

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)

    # Delete the image file
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], product.image))

    # Delete the product
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('index'))
