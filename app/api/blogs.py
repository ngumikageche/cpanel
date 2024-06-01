from flask import Blueprint, request, jsonify
from app import db
from models.usermodel import Blog  # Adjust import path based on your structure

blog_bp = Blueprint('blog', __name__, url_prefix='/blogs')

# Endpoint to create a new blog post
@blog_bp.route('/create', methods=['POST'])
def create_blog():
    data = request.json
    # Validate input data
    required_fields = ['title', 'content', 'user_id']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    new_blog = Blog(
        title=data['title'],
        content=data['content'],
        user_id=data['user_id']
    )

    db.session.add(new_blog)
    db.session.commit()

    return jsonify({'message': 'Blog post created successfully', 'blog_id': new_blog.id}), 201

# Endpoint to get a specific blog post
@blog_bp.route('/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    blog_dict = {
        'id': blog.id,
        'title': blog.title,
        'content': blog.content,
        'user_id': blog.user_id,
        'created_at': blog.created_at,
        'updated_at': blog.updated_at
    }
    return jsonify(blog_dict)

# Endpoint to update a blog post
@blog_bp.route('/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    data = request.json
    blog = Blog.query.get_or_404(blog_id)
    # Update blog attributes with the provided data
    if 'title' in data:
        blog.title = data['title']
    if 'content' in data:
        blog.content = data['content']

    db.session.commit()

    return jsonify({'message': 'Blog post updated successfully'})

# Endpoint to delete a blog post
@blog_bp.route('/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()
    return jsonify({'message': 'Blog post deleted successfully'})

# Endpoint to get all blog posts
@blog_bp.route('/', methods=['GET'])
def get_all_blogs():
    blogs = Blog.query.all()
    blogs_list = [{
        'id': blog.id,
        'title': blog.title,
        'content': blog.content,
        'user_id': blog.user_id,
        'created_at': blog.created_at,
        'updated_at': blog.updated_at
    } for blog in blogs]
    return jsonify(blogs_list)
