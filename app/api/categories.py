from flask import Blueprint, request, jsonify
from app import db
from models.usermodel import Category  # Adjust import path based on your structure

category_bp = Blueprint('category', __name__, url_prefix='/categories')

@category_bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    categories_list = [{'id': category.id, 'name': category.name} for category in categories]
    return jsonify(categories_list)

# Add routes for creating, updating, and deleting categories if needed
