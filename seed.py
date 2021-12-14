from models import *
from app import app

db.drop_all()
db.create_all()

# add core teams

team1 = CoreTeam(name='MICU')
team2 = CoreTeam(name='JMICU')
team3 = CoreTeam(name='ED')
team4 = CoreTeam(name='SICU')
team5 = CoreTeam(name='NICU')
team6 = CoreTeam(name='Charge')
team7 = CoreTeam(name='Ross')
team8 = CoreTeam(name='10ICU')
team9 = CoreTeam(name='NCCU')
team10 = CoreTeam(name='Floors')

team = [team1,team2,team3,team4,team5,team6,team7,team8,team9,team10]
for t in team:
  db.session.add(t)
db.session.commit()

# add  a few RT's

rt1 = RespStaff(first_name='Ryan', last_name='Tiller')
rt2 = RespStaff(first_name='Jamie', last_name='Zimmer', nick_name='JZ')
rt3 = RespStaff(first_name='Carolyn', last_name='Carny')
rt4 = RespStaff(first_name='Brian', last_name='Stiers')
rt5 = RespStaff(first_name='Shannan', last_name='Zerante')
rt6 = RespStaff(first_name='Kaylie', last_name='Arden')
rt7 = RespStaff(first_name='Courtney', last_name='Thompson')
rt8 = RespStaff(first_name='Taylor', last_name='Brown')
rt9 = RespStaff(first_name='Tara', last_name='Pain')
rt10 = RespStaff(first_name='Beatriz', last_name='Gonzolez')
rt11 = RespStaff(first_name='Sean', last_name='Callehan')
rt12 = RespStaff(first_name='David', last_name='Vascez')
rt13 = RespStaff(first_name='Law', last_name='Liermann')
rt14 = RespStaff(first_name='Stanley', last_name='Hendricks')
rt15 = RespStaff(first_name='Sara', last_name='Rindor')
rt16 = RespStaff(first_name='Cole', last_name='Morrison')
rt17 = RespStaff(first_name='Mollie', last_name='Howe')
rt18 = RespStaff(first_name='James', last_name='Stangle')
rt19 = RespStaff(first_name='Haley', last_name='Stangle')
rt20 = RespStaff(first_name='Heather', last_name='Forbush')
rt21 = RespStaff(first_name='Andrew', last_name='Rhidor', nick_name='Drew')
rt22 = RespStaff(first_name='Steve', last_name='Naggy')
rt23 = RespStaff(first_name='Amanda', last_name='Jennings')
rt24 = RespStaff(first_name='Abdoulaye', last_name='Ba BA')
rt25 = RespStaff(first_name='Akwasi', last_name='Amponsa-Sefa', nick_name='Q')
rt26 = RespStaff(first_name='Shawn', last_name='Biddle')
rt27 = RespStaff(first_name='Pam', last_name='Castle')
rt28 = RespStaff(first_name='Chhunheng', last_name='Chom', nick_name='Chom')
rt29 = RespStaff(first_name='Russel', last_name='Katterheinrich')
rt30 = RespStaff(first_name='Jarrod', last_name='Hume')

RTs = [rt1,rt2,rt3,rt4,rt5,rt6,rt7,rt8,rt9,rt10,rt11,rt12,rt13,rt14,rt15,rt16,rt17,rt18,rt19,rt20,rt21,rt22,rt23,rt24,rt25,rt26,rt27,rt28,rt29,rt30]
for rt in RTs:
  db.session.add(rt)
db.session.commit()

# add rt and core teams together
core1 = RTCoreTeam(rt_id=1,p_team_id=1, b_team_id=3, NICU=True, ED=True, Charge=True)
core2 = RTCoreTeam(rt_id=2,p_team_id=2, b_team_id=4)
core3 = RTCoreTeam(rt_id=3,p_team_id=1, b_team_id=2)
core4 = RTCoreTeam(rt_id=4,p_team_id=7, b_team_id=8)
core5 = RTCoreTeam(rt_id=5,p_team_id=2, b_team_id=8, NICU=True, ED=True, Charge=True)
core6 = RTCoreTeam(rt_id=6,p_team_id=4, b_team_id=4, NICU=True)
core7 = RTCoreTeam(rt_id=7,p_team_id=2, b_team_id=1)
core8 = RTCoreTeam(rt_id=8,p_team_id=1, b_team_id=2)
core9 = RTCoreTeam(rt_id=9,p_team_id=1, b_team_id=2, ED=True, Charge=True)
core10 = RTCoreTeam(rt_id=10,p_team_id=7, b_team_id=4, NICU=True)
core11 = RTCoreTeam(rt_id=11,p_team_id=7, b_team_id=4)
core12 = RTCoreTeam(rt_id=12,p_team_id=7, b_team_id=1)
core13 = RTCoreTeam(rt_id=13,p_team_id=4, b_team_id=7)
core14 = RTCoreTeam(rt_id=14,p_team_id=1, b_team_id=7)
core15 = RTCoreTeam(rt_id=15,p_team_id=10, b_team_id=10)
core16 = RTCoreTeam(rt_id=16,p_team_id=10, b_team_id=10)
core17 = RTCoreTeam(rt_id=17,p_team_id=10, b_team_id=1, NICU=True)
core18 = RTCoreTeam(rt_id=18,p_team_id=9, b_team_id=1)
core19 = RTCoreTeam(rt_id=19,p_team_id=9, b_team_id=1)
core20 = RTCoreTeam(rt_id=20,p_team_id=2, b_team_id=1, ED=True, Charge=True)
core21 = RTCoreTeam(rt_id=21,p_team_id=4, b_team_id=8)
core22 = RTCoreTeam(rt_id=22,p_team_id=7, b_team_id=1)
core23 = RTCoreTeam(rt_id=23,p_team_id=4, b_team_id=7, Charge=True)
core24 = RTCoreTeam(rt_id=24,p_team_id=8, b_team_id=1)
core25 = RTCoreTeam(rt_id=25,p_team_id=7, b_team_id=8)
core26 = RTCoreTeam(rt_id=26,p_team_id=2, b_team_id=1)
core27 = RTCoreTeam(rt_id=27,p_team_id=9, b_team_id=1, ED=True)
core28 = RTCoreTeam(rt_id=28,p_team_id=7, b_team_id=4)
core29 = RTCoreTeam(rt_id=29,p_team_id=2, b_team_id=9, ED=True)
core30 = RTCoreTeam(rt_id=30,p_team_id=2, b_team_id=1)




cores = [core1, core2, core3,core4,core5,core6,core7,core8,core9,core10,core11,core12,core13,core14,core15,core16,core17,core18,core19,core20,core21,core22,core23,core24,core25, core26,core27,core28,core29, core30]

for c in cores:
  db.session.add(c)
db.session.commit()

# add a restriction to test

rt_res = Restriction(rt_id=1, comment='tesing')

db.session.add(rt_res)
db.session.commit()

