from flask import Blueprint, request, jsonify
from extensions import db
from models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, get_jwt_identity
from datetime import timedelta

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
blacklist = set()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data.get('username') or not data.get('password'):
        return jsonify({'msg': 'Missing username or password'}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({'msg': 'User already exists'}), 409

    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'msg': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.username, expires_delta=timedelta(hours=1))
        return jsonify(access_token=access_token), 200

    return jsonify({'msg': 'Invalid username or password'}), 401

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    blacklist.add(jti)
    return jsonify(msg="Successfully logged out"), 200





