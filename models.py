
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True, nullable=False, index=True)
  first_name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  phone = db.Column(db.String(20), nullable=False)
  user_image = db.Column(db.String(200), nullable=False)
  password = db.Column(db.String(128), nullable=False)
  
  def set_password(self,password):
      self.password = generate_password_hash(password)
  
  def check_password(self,password):
      return check_password_hash(self.password_hash,password)
  

class UserRole(db.Model):
  __tablename__ = "user_role"
  id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.Integer, db.ForeignKey('user.id'))
  type =  db.Column(db.Integer, nullable=False)