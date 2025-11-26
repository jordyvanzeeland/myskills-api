from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True, nullable=False)
	username = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)

	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)
	
class SkillTypes(db.Model):
	__tablename__ = 'skilltypes'
	
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String, nullable=False)

	def to_dict(self):
		return {
            "id": self.id,
            "name": self.name
        }

class Skill(db.Model):
	__tablename__ = 'skills'
	
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String, nullable=False)
	type = db.Column(db.Integer, nullable=False)

	def to_dict(self):
		return {
            "id": self.id,
            "name": self.name,
			"type": self.type
        }