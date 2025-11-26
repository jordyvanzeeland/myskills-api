from flask import request, Blueprint
from flask_jsonpify import jsonify
from models import db, User, Skills
import jwt

skills = Blueprint('skills', __name__)

# Middleware function to check if the user is authenticated

@skills.before_request
def isAuthenticated():
    authtoken = request.headers.get('Authorization')

    if not authtoken:
        return jsonify({'error': 'No auth token in header'}), 400
    
    token = authtoken.split(' ')[1]
    payload = jwt.decode(token, 'secret', algorithms=['HS256'])

    user = User.query.filter_by(id=payload['id']).first()

    if not user:
        return jsonify({'error': 'Unauthorized'}), 400
    
# Function to get all skill
# Also you can filter on skill type giving a header skilltype

@skills.route('/', methods=['GET'])
def getAllSkills():
    try:
        typeid = request.headers.get('skilltype')

        if typeid:
            skills = Skills.query.filter_by(type=typeid)
        else:
            skills = Skills.query.all();
        
        data = [skill.to_dict() for skill in skills]
        
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 401
    
# Function to get a certain skill, given by it's ID
    
@skills.route('/type/<int:skillid>', methods=['GET'])
def getSkillByID(skillid):
    try:
        skill = Skills.query.filter_by(id=skillid).first()

        if not skill:
            return jsonify({'error': 'Skill not found'}), 400
        
        return jsonify(skill), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 401
    
# Function to insert a new skill
    
@skills.route('/insert', methods=['POST'])
def insertSkill():
    try:
        name = request.json.get('name')
        type = request.json.get('type')

        if not name or not type:
            return jsonify({'error': 'Name and Type are mandatory'}), 400
        
        new_skill = Skills(name=name, type=type)
        db.session.add(new_skill)
        db.session.commit()

        return jsonify({
            'message': 'New skill added', 
            "data": new_skill
        }), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 401
    
# Function to update a certain skill, given by ID
    
@skills.route('/<int:skillid>/update', methods=['PUT'])
def updateSkill(skillid):
    try:
        skill = Skills.query.filter_by(id=skillid).first()

        if not skill:
            return jsonify({'error': 'Skill not found'}), 400
        
        name = request.json.get('name')
        type = request.json.get('type')

        if not name or not type:
            return jsonify({'error': 'Name and Type are mandatory'}), 400
        
        skill.name = name
        skill.type = type
        db.session.commit()

        return jsonify({'message': 'Skill updated'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 401
    
# Function to delete a certain skill, given by ID
    
@skills.route('/<int:skillid>/delete', methods=['DELETE'])
def deleteSkill(skillid):
    try:
        skill = Skills.query.filter_by(id=skillid).first()

        if not skill:
            return jsonify({'error': 'Skill not found'}), 400
        
        db.session.delete(skill)
        db.session.commit()

        return jsonify({'message': 'Skill deleted'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 401