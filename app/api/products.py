from flask import Blueprint, request, jsonify, redirect, url_for, render_template, current_app
from werkzeug.utils import secure_filename
import os
from app import db
from models.usermodel import Product  # Adjust import path based on your structure

product_bp = Blueprint('product', __name__, url_prefix='/products')

@product_bp.route('/product/create', methods=['POST'])
def create_product():
    # Get form data
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    stock = request.form.get('stock')  # Assuming stock is also required
    category_id = request.form.get('category_id')  # Assuming category is required
    image = request.files.get('image')

    if not name or not description or not price or not stock or not category_id or not image:
        return jsonify({"error": "Missing required fields"}), 400

    # Save the image file
    filename = secure_filename(image.filename)
    image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    image.save(image_path)

    # Create a new product
    product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock,
        category_id=category_id,
        image=filename
    )
    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product created successfully", "product_id": product.id}), 201

@product_bp.route('/product/<int:id>', methods=['GET'])
def read_product(id):
    product = Product.query.get_or_404(id)
    return render_template('product.html', product=product)

@product_bp.route('/product/<int:id>', methods=['POST'])
def update_product(id):
    product = Product.query.get_or_404(id)

    # Update product fields
    product.name = request.form.get('name', product.name)
    product.description = request.form.get('description', product.description)
    product.price = request.form.get('price', product.price)
    product.stock = request.form.get('stock', product.stock)
    product.category_id = request.form.get('category_id', product.category_id)

    db.session.commit()

    return jsonify({"message": "Product updated successfully"}), 200

@product_bp.route('/product/<int:id>/image', methods=['POST'])
def update_product_image(id):
    product = Product.query.get_or_404(id)
    
    image = request.files.get('image')
    if image:
        # Delete the old image file
        old_image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], product.image)
        if os.path.exists(old_image_path):
            os.remove(old_image_path)

        # Save the new image file
        filename = secure_filename(image.filename)
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        # Update the image field
        product.image = filename

    db.session.commit()

    return jsonify({"message": "Product image updated successfully"}), 200

@product_bp.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)

    # Delete the image file
    image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], product.image)
    if os.path.exists(image_path):
        os.remove(image_path)

    # Delete the product
    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted successfully"}), 200

@product_bp.route('/', methods=['GET'])
def get_all_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    pagination = Product.query.paginate(page, per_page, False)
    products = pagination.items
    
    products_list = [{
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": str(product.price),
        "stock": product.stock,
        "category_id": product.category_id,
        "image": product.image
    } for product in products]

    return jsonify({
        "products": products_list,
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page
    }), 200

@product_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q', '')
    products = Product.query.filter(
        Product.name.ilike(f'%{query}%') | Product.description.ilike(f'%{query}%')
    ).all()
    
    products_list = [{
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": str(product.price),
        "stock": product.stock,
        "category_id": product.category_id,
        "image": product.image
    } for product in products]

    return jsonify(products_list), 200
