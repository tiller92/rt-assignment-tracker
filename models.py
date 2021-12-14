
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.expression import delete
from sqlalchemy.sql.schema import ForeignKey


db = SQLAlchemy()

#bcrypt = Bcrypt()

def connect_db(app):
    """connect to database"""
    db.app = app
    db.init_app(app)


class RespStaff(db.Model):
  """track staff names and nick names and shifts counts"""
  
  __tablename__ = 'respstaff'
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  
  first_name = db.Column(db.String(100), nullable=False)
  
  last_name = db.Column(db.String(100), nullable=False)
  
  nick_name = db.Column(db.String(50), nullable=True)
  
  shifts_in_p = db.Column(db.Integer, nullable=True,default=0)

  shifts_in_b = db.Column(db.Integer, nullable=True,default=0)
  
  shifts_in_tert = db.Column(db.Integer, nullable=True,default=0)
  
  shifts_on_floors = db.Column(db.Integer, nullable=True,default=0)
  
  total_shifts = db.Column(db.Integer, nullable=True, default=0)
  
  coreteams = db.relationship('RTCoreTeam', backref='respstaff', cascade="all,delete")
  
  restric = db.relationship('Restriction', backref='respstaff', cascade="all,delete")
  
  
  
class CoreTeam(db.Model):
  """list of core teams"""
  __tablename__ = 'CoreTeams'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  
  name = db.Column(db.String(50), nullable=False)
  
  
class RTCoreTeam(db.Model):
  """track RT core teams"""
  __tablename__ = 'RTCoreTeams'
  
  rt_id = db.Column(db.Integer, db.ForeignKey('respstaff.id'),primary_key=True, nullable=False)
  
  p_team_id = db.Column(db.Integer, nullable=False)
  
  b_team_id = db.Column(db.Integer, nullable=False)
  
  NICU = db.Column(db.Boolean, default=False, nullable=False)
  
  ED = db.Column(db.Boolean, default=False, nullable=False)
  
  Charge = db.Column(db.Boolean, default=False, nullable=False)
  
  
class Restriction(db.Model):
  """one floor people"""
  __tablename__ = 'Restrictions'
  
  rt_id = db.Column(db.Integer,db.ForeignKey('respstaff.id'), primary_key=True)
  
  comment = db.Column(db.String(250), nullable=True)