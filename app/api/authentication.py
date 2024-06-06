from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
from datetime import datetime, timedelta
from models.usermodel import User, Company  # Adjust import path based on your structure

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def generate_auth_token(user_id, company_id):
    payload = {
        'user_id': user_id,
        'company_id': company_id,
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiration time (e.g., 1 hour)
    }

    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token  # No need to decode, PyJWT v2+ returns a string

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    user = User.query.filter_by(username=username).first()
    if user:
        company_id = user.company_id
        company = Company.query.get(company_id)
        if company:
            if check_password_hash(user.password_hash, password):
                token = generate_auth_token(user.id, company.id)
                return jsonify({'token': token, 'company_id': company.id}), 200

    return jsonify({'error': 'Invalid username or password', 'data': data}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    # You can implement token invalidation logic here
    return jsonify({'message': 'Logged out successfully'}), 200

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    # Check if the email is already registered
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 400

    # You may want to add validation for the email format, password strength, etc.

    # Create a new user
    new_user = User(email=email, password_hash=generate_password_hash(password))

    # Save the new user to the database
    # db.session.add(new_user)
    # db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201
