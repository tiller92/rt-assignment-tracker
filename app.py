
from flask import Flask
from flask import render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import FileMultiDict
from functions import createStaffMemberDict, proccess_cell, staff_shift_count
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
import os
from models import db,connect_db, RespStaff, Restriction, RTCoreTeam, CoreTeam
from forms import GetFile, AddRT
from readxl import excel_break


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///rt_assignment'
# use secret key in production or default to our dev one
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'shh')
#below will connect to database after us set it up through heroku command line tools
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///flask-heroku')# use secret key in production or default to our dev one
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'shh')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)

  # home page where the assigments is submitted
@app.route('/', methods=['GET', 'POST'])
def home_page():
  form = GetFile()
  if form.validate_on_submit():
    file = form.file.data
    filename = secure_filename(file.filename)
    file.save(os.path.join(
            filename
        ))
    excel_result = excel_break(file)
    session['cur_assign'] = excel_result
    return redirect('/file-added')
  else:
    return render_template("index.html", form=form)
  
  

  # page that does the DB update but redirects 
@app.route('/file-added', methods=['POST','GET'])
def update_db():
  """do what you need with curr staff session"""
  alert = True
  curr_unit = ''
  for units in session['cur_assign']['units']:
    curr_unit = units
    staff_shift_count(session['cur_assign']['units'][curr_unit],curr_unit)
    # insert the time, date and shift the last file was added if time allows
  return render_template("index.html", alert=alert )


  #List all staff page
@app.route('/respstaff', methods=['GET','POST'])
def show_staff():
  stafflist = RespStaff.query.order_by(RespStaff.first_name.asc()).all()
  all_staff = []
  for person in stafflist:
    team_list = []
    extras = []
    team_list.append(CoreTeam.query.get_or_404(person.coreteams[0].p_team_id))
    team_list.append(CoreTeam.query.get_or_404(person.coreteams[0].b_team_id))
    extras.append(person.coreteams[0].NICU)
    extras.append(person.coreteams[0].ED)
    extras.append(person.coreteams[0].Charge)
    re = Restriction.query.get(person.id)
    all_staff.append(createStaffMemberDict(person,team_list, re,extras))
  return render_template('staff-table.html' , all_staff=all_staff) 

  
 # add staff only page
@app.route('/add-staff', methods=['GET','POST'])
def form_two():
  form = AddRT()
  if form.validate_on_submit():
    first_name = form.first_name.data
    last_name = form.last_name.data
    nick_name = form.nick_name.data
    primary = form.primary.data
    secondary = form.secondary.data
    ED = form.ED.data
    NICU = form.NICU.data
    Charge = form.Charge.data
    rest = form.restrictions.data
    NICU_bool = False
    ED_bool = False
    Charge_bool = False
    new_p_id = CoreTeam.query.filter_by(name=primary).one()
    new_s_id = CoreTeam.query.filter_by(name=secondary).one()
    if ED != None:
      ED_Bool =True
      
    if NICU != None:
      NICU_bool = True
      
    if Charge != None:
      Charge_bool=True
    # make commitments  
    new_rt = RespStaff(first_name=first_name, last_name=last_name, nick_name=nick_name)
    db.session.add(new_rt)
    db.session.commit()
    add_cores = RTCoreTeam(rt_id=new_rt.id, p_team_id=new_p_id.id, b_team_id=new_s_id.id,NICU=NICU_bool,ED=ED_bool, Charge=Charge_bool)
    if rest == str:
      new_res = Restriction(rt_id=new_rt.id, comment=rest)
      db.session.add(new_res)
    db.session.add(add_cores)
    db.session.commit()

    return redirect('/respstaff')
  else:
    return render_template("add-staff.html",  form=form)
  
  
  #form that edits staff
@app.route('/edit-staff/<int:id>', methods=['GET','POST'])
def edit_staff(id):
  rt = RespStaff.query.get(id)
  restrict = Restriction.query.filter_by(rt_id=id).first()
  form = AddRT(obj=rt)
  if form.validate_on_submit():  
    first_name = form.first_name.data
    last_name = form.last_name.data
    nick_name = form.nick_name.data
    primary = form.primary.data
    secondary = form.secondary.data
    ED = form.ED.data
    NICU = form.NICU.data
    Charge = form.Charge.data
    rest = form.restrictions.data
    NICU_bool = False
    ED_bool = False
    Charge_bool = False
   
    if ED != None and ED == 'ED':
      rt_teams = RTCoreTeam.query.filter_by(rt_id=id).first()
      print(rt_teams.ED)
      rt_teams.ED = True 
      db.session.add(rt_teams)
      db.session.commit()
      
      
    if NICU != None:
      rt_teams = RTCoreTeam.query.filter_by(rt_id=id).first()
      rt_teams.NICU = True 
      db.session.add(rt_teams)
      db.session.commit()
      
    if Charge != None:
      rt_teams = RTCoreTeam.query.filter_by(rt_id=id).first()
      rt_teams.Charge = True 
      db.session.add(rt_teams)
      db.session.commit()
    
    if first_name or last_name or nick_name:
      rt.first_name = first_name
      rt.last_name = last_name
      rt.nick_name = nick_name
      db.session.add(rt)
      db.session.commit()
   
    if primary or secondary:
      core_teams = RTCoreTeam.query.filter_by(rt_id=id).first()
      prime_id = CoreTeam.query.filter_by(name=primary).first()
      sec_id = CoreTeam.query.filter_by(name=secondary).first()
      core_teams.b_team_id = sec_id.id
      core_teams.p_team_id = prime_id.id
      
      db.session.add(core_teams)
      db.session.commit()
      
    if rest:
      if restrict.comment != rest:
        update_restriction = restrict.comment = rest
        db.session.add(update_restriction)
        db.session.commit()
      elif restrict == None and rest != None:
        new_restriction = Restriction(rt_id=id, comment=rest)
        db.session.add(new_restriction)
        db.session.commit()
    return redirect('/respstaff')
  else:
    return render_template("edit-staff.html",  form=form)
  
  
  # page that deletes staff from staff list 
@app.route('/remove-staff/<int:id>', methods=['POST'])
def remove_staff(id):
  rt = RespStaff.query.get(id)
  db.session.delete(rt)
  db.session.commit()
  return redirect('/respstaff')      


@app.route('/coreteams',methods=['GET','POST'])
def show_teams():
  
  team_dict = []
  
  return render_template('teams.html', teamdict=team_dict)