from common import *
@app.route('/addeve')
def reg_eve():
    if 'username' not in session:
        return redirect('/')
    else:   
        return render_template('addeve.html', row={})

@app.route('/alleve')
def alleve():
    if 'username' not in session:
        return redirect('/')
    else:   
        rows,msg = evemodel.get_eves(session['username'])
        return render_template('alleve.html', rows = rows, message=msg)

@app.route('/eve_disp')
def evedisp():
    if 'username' not in session:
        return redirect('/')
    else:
        rows,msg = evemodel.get_eves(session['username'])
        return render_template('evedisp.html', rows = rows, message=msg)

@app.route("/del_eve/<user>")
def del_eve(user):
  if 'username' in session:
    msg1 = evemodel.deleter(user)
    rows,msg = evemodel.get_eves(session['username'])
    return render_template('evedisp.html', rows = rows, message=msg)
  return redirect('/')

@app.route('/addrec_eve',methods = ['POST', 'GET'])
def addrec_eve():
    if 'username' not in session:
        return redirect('/')
    else:   
        if request.method == 'POST':
           res, msg, tday = evemodel.add_eve(request, session['username'])
           return render_template("everesult.html", result=res, message=msg, tday=tday)
        else:
           return render_template("addevent.html", row={})

@app.route('/editrec_eve',methods = ['POST', 'GET'])
def editrec_eve():
    if 'username' not in session:
        return redirect('/')
    else:   
        if request.method == 'POST':
            res, msg, tday = evemodel.edit_eve(request, session['username'])
            return render_template("everesult.html", result=dict(res), message=msg, tday=tday)
        else:
           return render_template("addeve.html", row={})

@app.route("/edit_eve/<user>")
def edit_eve(user):
  if 'username' in session:
    row, msg = evemodel.editor(user)
    return render_template('addeve.html', row = row)
  return redirect('/')

@app.route('/evesearch',methods = ['POST', 'GET'])
def search_eve():
    if 'username' not in session:
        return redirect('/')
    else:   
        if request.method == 'POST':
           res,msg = evemodel.searcheve(request, session['username'])
           return render_template("evedisp.html", rows=res, message=msg)
        else:
           rows, msg = evemodel.get_eves(session['username'])
           return render_template("evedisp.html", rows=rows)


@app.route('/evecal')
def evecal():
    if 'username' not in session:
        return redirect('/')
    else:
        ress = calendar.monthrange(datetime.datetime.now().year,datetime.datetime.now().month)
        liss = []
        for i in range(1,ress[1]+1):
          d = i
          if d < 10:
            d = str(0) + str(d)
          if datetime.datetime.now().month < 10:
            m = str(0) + str(datetime.datetime.now().month)
          pdate = str(datetime.datetime.now().year)+'-'+str(m)+'-'+str(d) 
          rows, msg =  evemodel.search1eve(pdate, session['username'])
          if len(rows) > 0:
            liss.append(d)
        return render_template('cal.html', first=ress[0], last=ress[1]+1, mon=datetime.datetime.now().month, yr=datetime.datetime.now().year, dy=datetime.datetime.now().day, liss=liss)

@app.route('/precal', methods = ['POST', 'GET'])
def precal():
    if 'username' not in session:
        return redirect('/')
    else:
        if request.method == 'POST':
            liss = []
            if int(request.form['mona']) > 1:
              y = int(request.form['yra'])
              m = int(request.form['mona'])-1
              ress = calendar.monthrange(y,m)
              for i in range(1,ress[1]+1):
                m = int(request.form['mona'])-1
                d = i
                if int(d) < 10:
                  d = str(0) + str(d)
                if int(m) < 10:
                  m = str(0) + str(m)
                pdate = str(y)+'-'+str(m)+'-'+str(d)
                rows, msg =  evemodel.search1eve(pdate, session['username'])
                if len(rows) > 0:
                  liss.append(i)
              return render_template('cal.html', first=ress[0], last=ress[1]+1, mon=int(m), yr=int(y), liss=liss)
            else:
              y = int(request.form['yra'])-1
              m = 12
              ress = calendar.monthrange(y,m)
              for i in range(1,ress[1]+1):
                m = 12
                d = i
                if int(d) < 10:
                  d = str(0) + str(d)
                if int(m) < 10:
                  m = str(0) + str(m)
                pdate = str(y)+'-'+str(m)+'-'+str(d) 
                rows, msg =  evemodel.search1eve(pdate, session['username'])
                if len(rows) > 0:
                  liss.append(i)
              return render_template('cal.html', first=ress[0], last=ress[1]+1, mon=int(m), yr=int(y), liss=liss)

@app.route('/nextcal', methods = ['POST', 'GET'])
def nextcal():
    if 'username' not in session:
        return redirect('/')
    else:
        if request.method == 'POST':
          liss = []
          if int(request.form['mona']) < 12:
            y = int(request.form['yra'])
            m = int(request.form['mona'])+1
            ress = calendar.monthrange(y,m)
            for i in range(1,ress[1]+1):
              m = int(request.form['mona'])+1
              d = i
              if int(d) < 10:
                d = str(0) + str(d)
              if int(m) < 10:
                m = str(0) + str(m)
              pdate = str(y)+'-'+str(m)+'-'+str(d)
              rows, msg =  evemodel.search1eve(pdate, session['username'])
              if len(rows) > 0:
                liss.append(i)
            return render_template('cal.html', first=ress[0], last=ress[1]+1, mon=int(m), yr=int(y), liss=liss)
          else:
            y = int(request.form['yra'])+1
            m = 1
            ress = calendar.monthrange(y,m)
            for i in range(1,ress[1]+1):
              m = 1
              d = i
              if int(d) < 10:
                d = str(0) + str(d)
              if int(m) < 10:
                m = str(0) + str(m)
              pdate = str(y)+'-'+str(m)+'-'+str(d) 
              rows, msg =  evemodel.search1eve(pdate, session['username'])
              if len(rows) > 0:
                liss.append(i)
            return render_template('cal.html', first=ress[0], last=ress[1]+1, mon=int(m), yr=int(y), liss=liss)

@app.route('/caleves/<int:d>')
@app.route('/caleves/<int:d>/<int:m>')
@app.route('/caleves/<int:d>/<int:m>/<int:y>')
def caleves(d, m=None, y=None):
    if 'username' not in session:
      return redirect('/')
    else:
      if d < 10:
        d = str(0) + str(d)
      if m < 10:
        m = str(0) + str(m)
      pdate = str(y)+'-'+str(m)+'-'+str(d) 
      rows, msg =  evemodel.search1eve(pdate, session['username'])
      return render_template('alleve.html', rows = rows, message=msg)
