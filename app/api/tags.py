from flask import Blueprint, request, jsonify
from app import db
from models.usermodel import Tag  # Adjust import path based on your structure

tag_bp = Blueprint('tag', __name__, url_prefix='/tags')

@tag_bp.route('/', methods=['GET'])
def get_tags():
    tags = Tag.query.all()
    tags_list = [{'id': tag.id, 'name': tag.name} for tag in tags]
    return jsonify(tags_list)

# Add routes for creating, updating, and deleting tags if needed
