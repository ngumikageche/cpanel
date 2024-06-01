from flask import Blueprint, request, jsonify
from app import db
from models.usermodel import User
from werkzeug.security import generate_password_hash

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{
        'id': user.id,
        'username': user.username,
        'company_email': user.company_email,
        'authentication_level': user.authentication_level,
        'status': user.status
    } for user in users]
    return jsonify(users_list)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    # Validate input data
    required_fields = ['username', 'company_email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Hash the password
    hashed_password = generate_password_hash(data['password'])

    new_user = User(
        username=data['username'],
        company_email=data['company_email'],
        password=hashed_password,
        authentication_level=data.get('authentication_level', 0),
        status=data.get('status', True)
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
        'company_email': user.company_email,
        'authentication_level': user.authentication_level,
        'status': user.status
    }
    return jsonify(user_dict)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.query.get_or_404(user_id)
    # Update user attributes with the provided data
    if 'username' in data:
        user.username = data['username']
    if 'company_email' in data:
        user.company_email = data['company_email']
    if 'password' in data:
        user.password = generate_password_hash(data['password'])
    if 'authentication_level' in data:
        user.authentication_level = data['authentication_level']
    if 'status' in data:
        user.status = data['status']

    db.session.commit()

    return jsonify({'message': 'User updated successfully'})

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})
