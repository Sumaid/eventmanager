import os
import sqlite3 as sql
import datetime
from dateutil import parser

def create():
 try:
   with sql.connect("evedata.db") as con:
 
     con.execute('''CREATE TABLE ttable (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   Category TEXT NOT NULL, 
                   Event TEXT NOT NULL, 
                   Location TEXT NOT NULL, 
                   Tdate TEXT NOT NULL,
                   Tday INT NOT NULL,
                   Ttime TEXT NOT NULL,
                   Description TEXT,
                   Owner TEXT NOT NULL,
                   ImgLink TEXT NOT NULL);''')

 except:
   print("table exists")   
def get_eves(uname):
  msg = "Records were fetched successfully"
  try:  
    with sql.connect("evedata.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * FROM ttable WHERE Owner='" + str(uname) + "'") 
      rows = cur.fetchall()
      return (rows,msg)
  except:
      return ([], "connection failed")
 
  
def add_eve(request, uname):
  try:
   cg = request.form['Category']
   ev = request.form['Event']
   lo = request.form['Location']
   td = request.form['EventDate']
   tt = request.form['EventTime']
   des = request.form['Description']
   cat2 = request.form['cat2']
   if cg == "others":
     cg = cat2
   wd = parser.parse(td).weekday()
   if 'file' not in request.files:
      myimg = 'static/default.png'
   else:
      img = request.files['file']
      myimg = 'static/' + str(uname) + str(td) + str(ev) + img.filename;
      img.save(myimg);
    
   msg = "Event successfully logged"
   with sql.connect("evedata.db") as con:
      cur = con.cursor()
      cur.execute("INSERT INTO ttable (Category,Event, Location, Tdate,Tday,Ttime, Description, Owner, ImgLink) VALUES (?,?,?, ?, ?, ?, ?, ?, ?)",
                 (cg,ev,lo,td,wd,tt,des,str(uname),myimg)) 
      con.commit()
      return  (request.form, msg, wd)
  except:
      msg = "Unexpected Error in insert operation"
      return ({}, msg, wd)

def delete_eve(request, uname):
 try:
   event = request.form['Event']
   tdate = request.form['EventDate']
   msg = "Record successfully deleted"
   with sql.connect("evedata.db") as con:
      cur = con.cursor()
      cur.execute("DELETE FROM ttable  WHERE Event='{0}' AND Tdate='{1}' AND Owner='{2}'".format(event, tdate, uname))
      con.commit()
      return (request.form, msg)
 except:
      msg = "error in delete operation"
      return ({}, msg)
 
def deleter(ide):
  try:
    msg = "Record successfully deleted"
    with sql.connect("evedata.db") as con:
      cur = con.cursor()
      cur.execute("DELETE FROM ttable WHERE ID='{0}'".format(ide))
      con.commit()
      return (request.form, msg)
  except:
      msg = "error in delete operation"
      return ({}, msg)

def search1eve(tdate1, uname):
 try:
   pdate = tdate1
   msg = "Events"
   with sql.connect("evedata.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * FROM ttable  WHERE Tdate='{0}' AND Owner='{1}'".format(pdate, uname))
      rows = cur.fetchall()
      return (rows,msg)
 except:
      msg = "Error in search operation"
      return ([],msg)


def searcheve(request, uname):
 try:
   pevent = request.form['keyword']
   pdate = request.form['pdate']
   plocation = request.form['plocation']
   pcat = request.form['pcat']   
   if pdate=="": 
     pdate="%"
   if pevent=="": 
     pevent="%"
   if plocation=="": 
     plocation="%"
   if pcat=="": 
     pcat="%"    

   msg = "Searching was successful"
   with sql.connect("evedata.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * FROM ttable  WHERE Event LIKE '{0}' AND Tdate LIKE '{1}' AND Location LIKE '{2}' AND Category LIKE '{3}' AND Owner='{4}'".format(pevent, pdate, plocation, pcat, uname))
#      cur.execute("SELECT * FROM ttable WHERE Owner='" + str(uname) + "'") 

      rows = cur.fetchall()
      return (rows,msg)
 except:
      msg = "Error in search operation"
      return ([],msg)

def editor(ide):
  try:
   msg = "Extracting was successful"
   with sql.connect("evedata.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * FROM ttable WHERE ID='" + ide + "'") 
      row = cur.fetchone()
      return (row,msg)    
  except:
    msg = "Error in extracting"
    return ({},msg)

def edit_eve(request, uname):
  try:
   cg = request.form['Category']
   ev = request.form['Event']
   lo = request.form['Location']
   td = request.form['EventDate']
   tt = request.form['EventTime']
   des = request.form['Description']
   ide = request.form['idee']
   cat2 = request.form['cat2']
   if cg == "others":
     cg = cat2
   wd = parser.parse(td).weekday()
   msg = "Event successfully edited"
   with sql.connect("evedata.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * FROM ttable WHERE ID='" + ide + "'")
      row = cur.fetchone()
      if cg=="":
        cg = row['Category']

      if ev=="":
        ev = row['Event'] 
      if lo=="":
        lo = row['Location']

      if td=="":
        td = row['Tdate']
      if tt=="":
        tt = row['Ttime']

      if des=="":
        des = row['Description']
      if wd ==0:
        wd =  row['Tday']

      if 'file' in request.files:
        img = request.files['file']
        myimg = 'static/' + str(uname) + str(td) + str(ev) + img.filename;
        img.save(myimg);
      else:
        myimg = row['ImgLink']



      cur.execute("""UPDATE ttable SET Category = ?, Event = ?, Location = ?, Tdate = ?, Tday = ?, Ttime = ?, Description = ?, Owner = ?, ImgLink = ? WHERE ID= ? """,
                 (cg,ev,lo,td,wd,tt,des,str(uname),myimg, request.form['idee'])) 
      con.commit()
      cur.execute("SELECT * FROM ttable WHERE ID='" + ide + "'")
      row = cur.fetchone()
      return  (row, msg, wd)
  except:
      msg = "Unexpected Error in edit operation"
      return ({}, msg, wd)
