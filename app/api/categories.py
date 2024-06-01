from flask import Blueprint, request, jsonify
from app import db
from models.usermodel import Category  # Adjust import path based on your structure

category_bp = Blueprint('category', __name__, url_prefix='/categories')

@category_bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    categories_list = [{'id': category.id, 'name': category.name} for category in categories]
    return jsonify(categories_list)

@category_bp.route('/create', methods=['POST'])
def create_category():
    name = request.form.get('name')

    if not name:
        return jsonify({"error": "Missing required field: name"}), 400

    category = Category(name=name)
    db.session.add(category)
    db.session.commit()

    return jsonify({"message": "Category created successfully", "category_id": category.id}), 201


@category_bp.route('/<int:id>/edit', methods=['PUT'])
def edit_category(id):
    category = Category.query.get_or_404(id)
    name = request.json.get('name')

    if not name:
        return jsonify({"error": "Missing required field: name"}), 400

    category.name = name
    db.session.commit()

    return jsonify({"message": "Category updated successfully"}), 200


@category_bp.route('/<int:id>/delete', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()

    return jsonify({"message": "Category deleted successfully"}), 200
