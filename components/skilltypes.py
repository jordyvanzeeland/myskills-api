from flask import request, Blueprint
from flask_jsonpify import jsonify
from models import db, User, SkillTypes
import jwt

skilltypes = Blueprint('skilltypes', __name__)

# Middleware function to check if the user is authenticated

@skilltypes.before_request
def isAuthenticated():
    authtoken = request.headers.get('Authorization')

    if not authtoken:
        return jsonify({'error': 'No auth token in header'}), 400
    
    token = authtoken.split(' ')[1]
    payload = jwt.decode(token, 'secret', algorithms=['HS256'])

    user = User.query.filter_by(id=payload['id']).first()

    if not user:
        return jsonify({'error': 'Unauthorized'}), 400
    
# Function to get all skills types

@skilltypes.route('/all', methods=['GET'])
def getAllTypes():
    try:
        types = SkillTypes.query.all();
        data = [type.to_dict() for type in types]
        
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 401
    
# Function to get a certain skills type, given by ID
    
@skilltypes.route('/<int:typeid>', methods=['GET'])
def getTypeByID(typeid):
    try:
        type = SkillTypes.query.filter_by(id=typeid).first()

        if not type:
            return jsonify({'error': 'Type not found'}), 400
        
        return jsonify(type), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 401
    
# Function to insert a new skills type
    
@skilltypes.route('/insert', methods=['POST'])
def insertType():
    try:
        name = request.json.get('name')

        if not name:
            return jsonify({'error': 'Empty type name'}), 400
        
        new_type = SkillTypes(name=name)
        db.session.add(new_type)
        db.session.commit()

        return jsonify({'message': 'New skills type added'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 401
    
# Function to update a certain skills type, given by ID
    
@skilltypes.route('/<int:typeid>/update', methods=['PUT'])
def updateType(typeid):
    try:
        skilltype = SkillTypes.query.filter_by(id=typeid).first()

        if not type:
            return jsonify({'error': 'Type not found'}), 400
        
        name = request.json.get('name')

        if not name:
            return jsonify({'error': 'Empty type name'}), 400
        
        skilltype.name = name
        db.session.commit()

        return jsonify({'message': 'Skills type updated'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 401
    
# Function to delete a certain skills type, given by ID
    
@skilltypes.route('/<int:typeid>/delete', methods=['DELETE'])
def deleteType(typeid):
    try:
        skilltype = SkillTypes.query.filter_by(id=typeid).first()

        if not type:
            return jsonify({'error': 'Type not found'}), 400
        
        db.session.delete(skilltype)
        db.session.commit()

        return jsonify({'message': 'Skills type deleted'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 401