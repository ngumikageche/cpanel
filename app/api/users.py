from flask import Blueprint, request, jsonify
from app import db
from models.usermodel import User, Company
from werkzeug.security import generate_password_hash

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'company': user.company_id,
        'pass': user.password_hash,
    } for user in users]
    return jsonify(users_list)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    
    # Validate input data
    required_fields = ['username', 'email', 'password', 'company_id']  # Add 'company_id' to required fields
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Hash the password
    hashed_password = generate_password_hash(data['password'])
    
    # Get company details
    company = Company.query.get(data['company_id'])
    if not company:
        return jsonify({'error': 'Company not found'}), 404
    
    # Create a new user associated with the company
    new_user = User(
        username=data['username'],
        email=data['email'],
        password_hash=hashed_password,
        company=company  # Associate the user with the company
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    user_dict = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
    }
    return jsonify(user_dict)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.query.get_or_404(user_id)
    # Update user attributes with the provided data
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.password_hash = generate_password_hash(data['password'])

    db.session.commit()

    return jsonify({'message': 'User updated successfully'})

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})
