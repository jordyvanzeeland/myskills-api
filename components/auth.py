from flask import request, Blueprint
from flask_jsonpify import jsonify
from models import db, User
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
import jwt

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
	try:
		username = request.json.get('username')
		password = request.json.get('password')

		if not username or not password:
			return jsonify({'error': 'Username and password are required'}), 400
		
		user = User.query.filter_by(username=username).first()

		if user is None or not check_password_hash(user.password, password):
			return jsonify({'error': 'Unauthorized, incorrect username or password'}), 401
		
		payload = {
				'id': user.id,
				'username': user.username,
				'email': user.email,
				'exp': datetime.utcnow() + timedelta(hours=1), 
				'iat': datetime.utcnow(),
			}

		token = jwt.encode(payload, 'secret', algorithm='HS256')

		return jsonify({
			'user': {
				'id': user.id,
				'username': user.username,
				'email': user.email
			},
			'token': token
		}), 200
	except Exception as e:
		return jsonify({'error': e}), 401

@auth.route('/register', methods=['POST'])
def register():
	try:
		username = request.json.get('username')
		email = request.json.get('email')
		password = request.json.get('password')

		if User.query.filter_by(username=username).first():
			return jsonify({'error': 'Username already exists'}), 409
	
		if User.query.filter_by(email=email).first():
			return jsonify({'error': 'email already exists'}), 409
		
		new_user = User(
			username=username,
			email=email
		)
		new_user.set_password(password)

		db.session.add(new_user)
		db.session.commit()
		return jsonify({'message': 'User registered successfully'}), 201
	except Exception as e:
		return jsonify({'error': e}), 401