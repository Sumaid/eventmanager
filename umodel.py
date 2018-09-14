import sqlite3 as sql
import hashlib
def create():
    try:
        with sql.connect("users.db") as con:
            print ("Opened database successfully")
 
        con.execute('''CREATE TABLE Users (username TEXT NOT NULL, 
                   password TEXT NOT NULL,
                   contact TEXT NOT NULL,
                   email TEXT NOT NULL) 
                    ;''')
        
        print ("Users Table created successfully")
    
    except:
        print ("Users Table already exists")

def check_password(hashed, user_pass):
    return hashed == hashlib.md5(user_pass.encode()).hexdigest()

def validate(username,password):
    con = sql.connect('users.db')
    completion = False
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Users")
        rows = cur.fetchall()
        for row in rows:
            dbUser = row[0]
            dbPass = row[1]
            if dbUser==username:
                completion=check_password(dbPass, password)
    return completion

def validate_admin(username,password):
    con = sql.connect('admins.db')
    completion = False
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Admins")
        rows = cur.fetchall()
        for row in rows:
            dbUser = row[0]
            dbPass = row[1]
            if dbUser==username:
                completion=check_password(dbPass, password)
    return completion

def getAll():
  msg = "Records were fetched successfully"
  try:  
    with sql.connect("users.db") as con:
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("select * from Users where username is not null")
      rows = cur.fetchall()
      for row in rows:
           print (row["username"])
      return (rows,msg)
  except:
      print ("connection failed")
      return ([], "connection failed")
 
  
def addUser(request):
  try:
    name = request.form['nm']
    hashed_pass = hashlib.md5(request.form['pswd'].encode()).hexdigest()
    contact = request.form['cntct']
    email= request.form['email']
    
    msg = "You are succesfully registered!"
    
    con = sql.connect('users.db')
    error = False
    with con:
      cur = con.cursor()
      cur.execute("SELECT * FROM Users")
      rows = cur.fetchall()
      for row in rows:
        dbUser = row[0]
        if(dbUser==name):
          msg = "User with name %s is already present, insertion failed!"%name
          error = True
    
    if not error:
      cur.execute("INSERT INTO Users (username, password, contact, email)  VALUES (?,?,?,?)",(name, hashed_pass, contact, email))            
      con.commit()
    return  (request.form, msg,error)
    

  except:
      msg = "Unexpected Error in insert operation"
      print (msg)
      return ({}, msg)

def deleteUser(request):
 try:
   user = request.form['nm']
   msg = "Record successfully deleted"
   with sql.connect("users.db") as con:
      cur = con.cursor()
      cur.execute("DELETE FROM Users WHERE username='" + str(user) + "'")
      con.commit()
      print ("user deleted")
      return (request.form, msg)
 except:
      msg = "error in delete operation"
      print ("in delete - exception handler")
      return ({}, msg)

def deluser(uname):
 try:
   with sql.connect("users.db") as con:
      cur = con.cursor()
      cur.execute("DELETE FROM Users WHERE username='" + str(uname) + "'")
      con.commit()
      print ("user deleted")
      return msg
 except:
      msg = "error in delete operation"
      print ("in delete - exception handler")
      return msg  
