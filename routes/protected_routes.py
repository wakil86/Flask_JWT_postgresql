from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

protected_bp = Blueprint('protected', __name__, url_prefix='/protected')

@protected_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()
    return jsonify(message=f"Welcome {current_user}, this is your dashboard"), 200
