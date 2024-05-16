#api.users
from flask import Blueprint, request, jsonify
from app import db
from models.usermodel import User

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    # Logic to fetch users from the database
    users = User.query.all()

    # Convert users to a list of dictionaries
    users_list = []
    for user in users:
        users_list.append({
            'id': user.id,
            'username': user.username,
            'company_email': user.company_email,
            'authentication_level': user.authentication_level,
            'status': user.status
        })

    # Return users as JSON
    return jsonify(users_list)


# Define route for creating a new user
@user_bp.route('/users', methods=['POST'])
def create_user():
    # Parse JSON data from the request
    data = request.json

    # Extract required fields from the JSON data
    username = data.get('username')
    company_email = data.get('company_email')
    password = data.get('password')
    authentication_level = data.get('authentication_level', 0)  # Default value if not provided
    status = data.get('status', True)  # Default value if not provided

    # Create a new User object
    new_user = User(
        username=username,
        company_email=company_email,
        password=password,
        authentication_level=authentication_level,
        status=status
    )

    # Add the new user to the session and commit to save to the database
    db.session.add(new_user)
    db.session.commit()

    # Return a response indicating success
    return jsonify({'message': 'User created successfully'}), 201  # 201 indicates successful creation

# Define route for getting a specific user
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Fetch the user from the database by user_id
    user = User.query.filter_by(id=user_id).first()

    # Check if user exists
    if user:
        # Convert user to a dictionary
        user_dict = {
            'id': user.id,
            'username': user.username,
            'company_email': user.company_email,
            'authentication_level': user.authentication_level,
            'status': user.status
        }
        return jsonify(user_dict)
    else:
        # If user with given user_id does not exist, return a 404 error
        return jsonify({'error': 'User not found'}), 404

# Define route for updating a user
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Parse JSON data from the request
    data = request.json

    # Fetch the user from the database by user_id
    user = User.query.get(user_id)

    # Check if user exists
    if user:
        # Update user attributes with the provided data
        if 'username' in data:
            user.username = data['username']
        if 'company_email' in data:
            user.company_email = data['company_email']
        if 'password' in data:
            user.password = data['password']
        if 'authentication_level' in data:
            user.authentication_level = data['authentication_level']
        if 'status' in data:
            user.status = data['status']

        # Commit the changes to the database
        db.session.commit()

        # Return a response indicating success
        return jsonify({'message': 'User updated successfully'})
    else:
        # If user with given user_id does not exist, return a 404 error
        return jsonify({'error': 'User not found'}), 404

# Define route for deleting a user
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Fetch the user from the database by user_id
    user = User.query.get(user_id)

    # Check if user exists
    if user:
        # Delete the user from the database
        db.session.delete(user)
        db.session.commit()

        # Return a response indicating success
        return jsonify({'message': 'User deleted successfully'})
    else:
        # If user with given user_id does not exist, return a 404 error
        return jsonify({'error': 'User not found'}), 404

# if __name__ == '__main__':
#     app.run(debug=True)
