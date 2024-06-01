from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
from datetime import datetime, timedelta
from models.usermodel import User  # Adjust import path based on your structure

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid username or password'}), 401

    token = jwt.encode({'user_id': user.id, 'exp': datetime.utcnow() + timedelta(hours=1)},
                       current_app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token.decode('utf-8')}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    # You can implement token invalidation logic here
    return jsonify({'message': 'Logged out successfully'}), 200
