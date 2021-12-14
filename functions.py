"""File contains vital funciotns for staffing break down"""

import flask_sqlalchemy
from sqlalchemy.util.langhelpers import NoneType
from models import CoreTeam, Restriction


def createStaffDict():
  """takes all the tables in and creates a comprehenisive dict off all important data"""
  staffdict = {
    'RT':{
      'id':0,
      'first_name':'',
      'last_name':'',
      'nick_name':'',
      'coreteams':{
        'primary':{
          'name':'',
          'numshifts':0,
          },
        'secondary': {
          'name':'',
          'numshifts':0,
          },
         'Floors':{
          'numshifts':0,
          },
        'NICU':{
          'trained':False,
          'numshifts':0,
          },
         'ED':{
          'trained':False,
          'numshifts':0,
          },
          'Charge':{
          'trained':False,
          'numshifts':0,
          },},
      'Restriction':{
        'restriction':False,
        'comment':'',
        }
      }  
    }
  
  return staffdict

def createStaffMemberDict(member, member_teams, restriction,extras):
  
  print(extras)
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
          'numshifts':0,
          },
        'secondary': {
          'name':member_teams[1].name,
          'numshifts':0,
          },
         'Floors':{
          'numshifts':0,
          },
        'NICU':{
          'trained':extras[0],
          'numshifts':0,
          },
         'ED':{
          'trained':extras[1],
          'numshifts':0,
          },
          'Charge':{
          'trained':extras[2],
          'numshifts':0,
          },},
      'Restriction':{
        'restriction':restriction_y,
        'comment':restriction_x,
        }
      }  
    }
  
  return staffdict


