import sqlite3 as sql
import datetime
from dateutil import parser

def create():
 try:
   with sql.connect("expdata.db") as con:
     print ("Opened database successfully")
 
     con.execute('''CREATE TABLE ttable ( 
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   Category TEXT NOT NULL, 
                   Expenditure TEXT NOT NULL, 
                   Location TEXT NOT NULL, 
                   Tdate TEXT NOT NULL,
                   Tday INT NOT NULL,
                   Ttime TEXT NOT NULL,
                   Price INT,
                   Owner TEXT NOT NULL);''')

     print ("Table created successfully")
 except:
   print ("Table already exists")

def get_exps(uname):
  msg = "Records were fetched successfully"
  try:  
    with sql.connect("expdata.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * FROM ttable WHERE Owner='" + str(uname) + "'") 
      rows = cur.fetchall()
      return (rows,msg)
  except:
      print ("connection failed")
      return ([], "connection failed")
 
  
def add_exp(request, uname):
  try:
   cg = request.form['Category']
   ev = request.form['Expenditure']
   lo = request.form['Location']
   td = request.form['ExpDate']
   tt = request.form['ExpTime']
   pr = request.form['Price']
   cat2 = request.form['cat2']
   if cg == "others":
     cg = cat2   
   wd = parser.parse(td).weekday()
   msg = "Record successfully added"
   with sql.connect("expdata.db") as con:
      con.row_factory = sql.Row
      print('LLLLLLLLLLLLLL')
      cur = con.cursor()
      cur.execute("INSERT INTO ttable (Category , Expenditure, Location, Tdate,Tday, Ttime, Price, Owner) VALUES (?,?,?, ?, ?, ?, ?, ?)",
                 (cg,ev, lo, td, wd,tt, int(pr), str(uname))) 
      con.commit()
      print (msg)
      return  (request.form, msg, wd)
  except:
      msg = "Unexpected Error in insert operation"
      print (msg)
      return ({}, msg, wd)

def deleter(ide):
  try:
    msg = "Record successfully deleted"
    with sql.connect("expdata.db") as con:
      cur = con.cursor()
      cur.execute("DELETE FROM ttable WHERE ID='{0}'".format(ide))
      con.commit()
      return (request.form, msg)
  except:
      msg = "error in delete operation"
      return ({}, msg)

def search1exp(tdate1, uname):
 try:
   pdate = tdate1
   msg = "Expenditures"
   with sql.connect("expdata.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * FROM ttable  WHERE Tdate='{0}' AND Owner='{1}'".format(pdate, uname))
      rows = cur.fetchall()
      print('Trouble')
      for  row in rows:
        print(row['Category'])
      print("Search wala")
      print(rows)
      return (rows,msg)
 except:
      print("Life sucks")
      msg = "Error in search operation"
      return ([],msg)

def searchexp(request, uname):
 try:
   pevent = request.form['keyword']
   pdate = request.form['pdate']
   plocation = request.form['plocation']
   pcat = request.form['pcat']
   pl = request.form['lprice']
   pu = request.form['uprice']   
   if pdate=="": 
     pdate="%"
   if pevent=="": 
     pevent="%"
   if plocation=="": 
     plocation="%"
   if pcat=="": 
     pcat="%"    
   if pl == "":
     pl=0
   if pu == "":
     pu=1000000 
   print("Life here is good:")
   print(pevent)
   print(pdate)
   print(plocation)
   print(pcat)
   print(uname)
   msg = "Searching was successful"
   with sql.connect("expdata.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * FROM ttable  WHERE Expenditure LIKE '{0}' AND Tdate LIKE '{1}' AND Location LIKE '{2}' AND Category LIKE '{3}' AND Owner='{4}' AND PRICE BETWEEN {5} AND {6}".format(pevent, pdate, plocation, pcat, uname, pl, pu))
#      cur.execute("SELECT * FROM ttable WHERE Owner='" + str(uname) + "'") 

      rows = cur.fetchall()

      print(rows)
      return (rows,msg)
 except:
      msg = "Error in search operation"
      return ([],msg)

def editor(ide):
  try:
   msg = "Extracting was successful"
   with sql.connect("expdata.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * FROM ttable WHERE ID='" + ide + "'") 
      row = cur.fetchone()
      print(row)
      return (row,msg)    
  except:
    msg = "Error in extracting"
    return ({},msg)

def edit_exp(request, uname):
  try:
   cg = request.form['Category']
   ev = request.form['Expenditure']
   lo = request.form['Location']
   td = request.form['ExpDate']
   tt = request.form['ExpTime']
   des = request.form['Price']
   ide = request.form['idee']
   cat2 = request.form['cat2']
   if cg == "others":
     cg = cat2   
   wd = parser.parse(td).weekday()
   print(request.form)
   msg = "Expenditure successfully edited"
   with sql.connect("expdata.db") as con:
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

      if des==0:
        des = row['Price']
      if wd ==0:
        wd =  row['Tday']

      cur.execute("""UPDATE ttable SET Category = ?, Expenditure = ?, Location = ?, Tdate = ?, Tday = ?, Ttime = ?, Price = ?, Owner = ? WHERE ID= ? """,
                 (cg,ev,lo,td,wd,tt,des,str(uname),request.form['idee'])) 
      con.commit()
      print (msg)
      return  (request.form, msg, wd)
  except:
      msg = "Unexpected Error in edit operation"
      print (msg)
      return ({}, msg, wd)