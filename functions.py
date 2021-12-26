"""File contains vital funciotns for staffing break down"""

from os import error
from typing import final
from sqlalchemy.util.langhelpers import NoneType, attrsetter
from models import CoreTeam, RespStaff, Restriction, connect_db,db



def createStaffMemberDict(member, member_teams, restriction,extras):

  if type(restriction) != NoneType:
    restriction_y = True
    restriction_x = restriction.comment
  else:
    restriction_y = False
    restriction_x = ''

  staffdict = {
    'RT':{
      'id':member.id,
      'first_name':member.first_name,
      'last_name':member.last_name,
      'nick_name':member.nick_name,
      'coreteams':{
        'primary':{
          'name':member_teams[0].name,
          'numshifts':member.shifts_in_p,
          },
        'secondary': {
          'name':member_teams[1].name,
          'numshifts':member.shifts_in_b,
          },
        'tert':{
          'numshifts':member.shifts_in_tert,
        },
         'Floors':{
          'numshifts':member.shifts_on_floors,
          },
        'NICU':{
          'trained':extras[0],
          'numshifts':member.shifts_in_NICU,
          },
         'ED':{
          'trained':extras[1],
          'numshifts':member.shifts_in_ED,
          },
          'Charge':{
          'trained':extras[2],
          'numshifts':member.shifts_in_Charge,
          },},
      'Restriction':{
        'restriction':restriction_y,
        'comment':restriction_x,
        }
      }  
    }
  
  return staffdict


def proccess_cell(str):
    """look for slashes and nums and returns an arr of strings with the rt in that assignment. only filters by / and -- no other symbols at this time. This is called in the staff_shift_count()"""
    str_p = str.rsplit('/')
    arr_str = []
    strip_arr = []
    alpha_arr = []
    final_list = []
  
   
    for i in str_p:
      if i.find('4') > -1:
        no_4_str =i.replace('4', '')
        arr_str.append(no_4_str)
      elif i.find('8') > -1:
        no_8_str = i.replace('8', '')
        arr_str.append(no_8_str)
      else:
        arr_str.append(i)

    for i in arr_str:
      if '8' in i or '4' in i:
        arr_str.remove(i)
    
    for i in arr_str:
      split_str = i.strip()
      strip_arr.append(split_str)
 
    for i in strip_arr:
      if i.isalpha() is False:
        strip_arr.remove(i)
      else:
        alpha_arr.append(i)

    for i in strip_arr:
      if i.find('-') != -1:
        strip_arr.remove(i)

    for i in strip_arr:
      if i not in final_list:
        final_list.append(i)
  
    return final_list
  
  
def staff_shift_count(arr,core_team):
  """"recieves the unit array and then add to the person shift count"""
  unit = []
  unit_id = CoreTeam.query.filter_by(name=core_team).first()
  
  for cell in arr:
    staff = proccess_cell(cell)
    for person in staff:
      unit.append(person)
      
  
  for name in unit:
    
    RT = RespStaff.query.filter_by(first_name=name).first()
    
    if RT == None:
      print(f"{name} is not in DB")
      try:
        RT = RespStaff.query.filter_by(nick_name=name).first()
        print('nickname found')
      except:
        print('no nick name')
    else:
      try:
        if RT.coreteams[0].p_team_id == unit_id.id:
          RT.shifts_in_p += 1
          db.session.commit()
        elif RT.coreteams[0].b_team_id == unit_id.id:
          RT.shifts_in_b += 1
          db.session.commit()
        elif core_team == 'NICU' and RT.coreteams[0].NICU == True:
          RT.shifts_in_NICU += 1
          RT.shifts_in_tert += 1
          db.session.commit()
        elif core_team == 'ED' and RT.coreteams[0].ED == True:
          RT.shifts_in_ED += 1
          RT.shifts_in_tert += 1
          db.session.commit()
        elif core_team == 'Charge' and RT.coreteams[0].Charge == True:
          RT.shifts_in_Charge += 1
          RT.shifts_in_tert += 1
          db.session.commit()
        elif core_team == 'FLOORS':
          RT.shifts_on_floors += 1
          db.session.commit()
      except:
        print(RT.first_name, RT.id, 'error', core_team, unit_id)



def sort_staff(obj, sort_by):
  asc_staff = sorted(obj['RT']['first_name'])
  print(asc_staff)