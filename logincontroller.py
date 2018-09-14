from common import *
@app.route("/")
def index():
   if 'username' in session:
        return redirect('/userhome')
   
   elif 'adminname' in session:
        return redirect('/admin_home')
   
   return render_template("index.html")

@app.route("/userhome")
def user_home():
    if 'username' not in session:
        return redirect('/')

    return render_template("userhome.html", uname=session['username'])

@app.route('/register')
def register():
   if 'username' in session:
        return redirect('/userhome')
   
   return render_template('adduser.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if 'username' in session:
        return redirect('/userhome')
   else:
       if request.method == 'POST':
          res, msg,err = umodel.addUser(request)
          if err:
            flash(u'Username is already taken , please choose another username','register')
          else:
            flash(u'You have successfully registered , login to proceed','register')

          #return render_template("result.html", result=res, message=msg)
          return redirect('/')

@app.route('/login',methods=['POST','GET'])
def login():
    if 'username' in session:
        return redirect('/userhome')
    else:    
        error = None
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            completion = umodel.validate(username, password)
            if completion == False:
                error = 'Invalid Credentials. Please try again.'
            else:
                session['username'] = username
                return redirect('/userhome')
        flash('Invalid User Login Credentials','user')
        return redirect('/')   


@app.route('/logout')
def logout():
  if 'username' in session:	
    session.pop('username',None)
  elif 'adminname' in session:
    session.pop('adminname',None)

  return redirect('/')
