from common import *
from expensecontroller import *
from eventcontroller import *
from logincontroller import *

@app.route("/calendar")
def cal():
  if 'username' in session:
    rows,msg = evemodel.get_eves(session['username'])
    temp,mpg = expmodel.get_exps(session['username'])
    return render_template("calendar.html",evrows=rows, exrows=temp, evmessage=msg, exmessage=mpg)

  return redirect('/')

#----------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------
@app.route("/calendar/<user>")
def acal(user):
  if 'adminname' in session:
    rows,msg = evemodel.get_eves(user)
    temp,mpg = expmodel.get_exps(user)

    return render_template("calendar.html",evrows=rows, exrows=temp, evmessage=msg, exmessage=mpg)
  
  return redirect('/')

@app.route("/del/<user>")
def adel(user):
  if 'adminname' in session:
    msg1 = umodel.deluser(user)
    rows,msg = umodel.getAll()
    return render_template('showall.html', rows = rows, message=msg)
  return redirect('/')

@app.route('/showall')
def showall():
   rows,msg = umodel.getAll()
   return render_template('showall.html', rows = rows, message=msg)

@app.route("/admin_home")
def admin_home():
    if 'adminname' not in session:
        return redirect('/')

    return render_template("adminhome.html")


@app.route('/alogin',methods=['POST','GET'])
def alogin():
    if 'username' in session:
        return redirect('/userhome')	
    elif 'adminname' in session:
        return redirect('/admin_home')	

    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = umodel.validate_admin(username, password)
        if completion == False:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['adminname'] = username
            return redirect('/admin_home')
    
    flash(u'Invalid Admin Login Credentials','admin')
    return redirect('/')    

#------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
             
if __name__ == '__main__':
   app.run(debug = True)
