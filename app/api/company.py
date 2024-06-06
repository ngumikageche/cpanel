# Import necessary modules
from flask import Blueprint, request, jsonify
from app import db
from models.usermodel import Company

# Create a Blueprint for companies
company_bp = Blueprint('company', __name__, url_prefix='/companies')

# Route for creating a new company
@company_bp.route('/', methods=['POST'])
def create_company():
    data = request.json
    
    # Validate input data
    required_fields = ['name', 'description', 'industry', 'founded_at']  # Add other required fields
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Create a new company
    new_company = Company(
        name=data['name'],
        description=data['description'],
        industry=data['industry'],
        founded_at=data['founded_at'],
        headquarters=data.get('headquarters'),  # Optional field
        website=data.get('website')  # Optional field
    )

    db.session.add(new_company)
    db.session.commit()

    return jsonify({'message': 'Company created successfully', 'company_id': new_company.id}), 201

# Route for getting all companies
@company_bp.route('/', methods=['GET'])
def get_all_companies():
    companies = Company.query.all()
    companies_list = [{
        'id': company.id,
        'name': company.name,
        'description': company.description,
        'industry': company.industry,
        'founded_at': company.founded_at.strftime('%Y-%m-%d'),  # Convert datetime to string
        'headquarters': company.headquarters,
        'website': company.website
    } for company in companies]
    return jsonify(companies_list)

# Other routes for updating, deleting, and getting a single company...

# Return the company blueprint
