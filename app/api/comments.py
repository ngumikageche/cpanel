from flask import Blueprint, request, jsonify
from app import db
from models.usermodel import Comment  # Adjust import path based on your structure

comment_bp = Blueprint('comment', __name__, url_prefix='/comments')

@comment_bp.route('/create', methods=['POST'])
def create_comment():
    data = request.json
    content = data.get('content')
    user_id = data.get('user_id')
    blog_id = data.get('blog_id')

    if not content or not user_id or not blog_id:
        return jsonify({'error': 'Missing required fields'}), 400

    new_comment = Comment(content=content, user_id=user_id, blog_id=blog_id)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({'message': 'Comment created successfully', 'comment_id': new_comment.id}), 201

# Add routes for reading, updating, and deleting comments if needed
    