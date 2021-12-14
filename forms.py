"""this is the template for WTFforms to create forms. Pass in FlaskForm into the form class you wish to creae"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, TextAreaField, FileField,RadioField, SelectField,SelectMultipleField
from wtforms.validators import InputRequired, Optional, Email, Length
from flask_wtf.file import FileField, FileRequired

class GetFile(FlaskForm):
     file = FileField('excel-file', validators=[FileRequired()])
  

class AddRT(FlaskForm):
  
  first_name = StringField('First name', validators=[InputRequired()])
  
  last_name = StringField('Last name', validators=[InputRequired()])
  
  nick_name = StringField('Nickname' ,validators=[Optional()])
                          
  primary = SelectField('Core Team Primary', choices=['MICU','JMICU','SICU', 'Ross', '10ICU','NCCU','Floors'],validators=[Optional()])
  
  secondary = SelectField('Core Team Secondary', choices=['MICU','JMICU','SICU', 'Ross','NCCU', '10ICU','Floors'],validators=[Optional()])
  
  ED = RadioField('ED',choices=['ED'],validators=[Optional()])
   
  NICU = RadioField('NICU',choices=['NICU'],validators=[Optional()])
   
  Charge = RadioField('Charge',choices=['Charge'],validators=[Optional()])
  
  restrictions =  StringField('Restrictions', validators=[Optional()])
  
  