from common import *

@app.route('/exptime')
def exptime():
    if 'username' not in session:
        return redirect('/')
    else:
        ress = calendar.monthrange(datetime.datetime.now().year,datetime.datetime.now().month)
        liss = []
        liss1 = {}
        liss1 = defaultdict(lambda: 0, liss1)
        liss2 = {}
        sum1 = []
        sum2 = []
        for i in range(1,ress[1]+1):
          d = i
          if d < 10:
            d = str(0) + str(d)
          if datetime.datetime.now().month < 10:
            m = str(0) + str(datetime.datetime.now().month)
          pdate = str(datetime.datetime.now().year)+'-'+str(m)+'-'+str(d) 
          rows, msg =  expmodel.search1exp(pdate, session['username'])
          cost = 0
          for row in rows:
            cost = cost + row['Price']
            catc = str(row["Category"])
            liss1[catc] = int(liss1[catc]) + int(row['Price'])
          liss.insert(i+1, cost)
        j = 0
        for key in liss1.keys():
          sum1.insert(j, key)
          sum2.insert(j, liss1[key])
          j = j+1

        return render_template('cale.html', first=ress[0], last=ress[1]+1, mon=datetime.datetime.now().month, yr=datetime.datetime.now().year, dy=datetime.datetime.now().day, liss = liss, sum1 = sum1, sum2 = sum2, ind=j)

@app.route('/preexp', methods = ['POST', 'GET'])
def preexp():
    if 'username' not in session:
        return redirect('/')
    else:
        if request.method == 'POST':
            liss = []
            liss1 = {}
            liss1 = defaultdict(lambda: 0, liss1)
            liss2 = {}
            sum1 = []
            sum2 = []
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
                rows, msg =  expmodel.search1exp(pdate, session['username'])
                cost = 0
                for row in rows:
                  catc = str(row["Category"])
                  liss1[catc] = int(liss1[catc]) + int(row['Price'])  
                  cost = cost + row['Price']
                liss.insert(i, cost)
              j = 0
              for key in liss1.keys():
                sum1.insert(j, key)
                sum2.insert(j, liss1[key])
                j = j+1
              return render_template('cale.html', first=ress[0], last=ress[1]+1, mon=int(m), yr=int(y), dy=datetime.datetime.now().day, liss = liss, sum1 = sum1, sum2 = sum2, ind=j)
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
                rows, msg =  expmodel.search1exp(pdate, session['username'])
                cost = 0
                for row in rows:
                  catc = str(row["Category"])
                  liss1[catc] = int(liss1[catc]) + int(row['Price'])  
                  cost = cost + row['Price']
                liss.insert(i, cost)
              j = 0
              for key in liss1.keys():
                sum1.insert(j, key)
                sum2.insert(j, liss1[key])
                j = j+1
              return render_template('cale.html', first=ress[0], last=ress[1]+1, mon=int(m), yr=int(y), dy=datetime.datetime.now().day, liss = liss, sum1 = sum1, sum2 = sum2, ind=j)

@app.route('/nextexp', methods = ['POST', 'GET'])
def nextexp():
    if 'username' not in session:
        return redirect('/')
    else:
        if request.method == 'POST':
          liss = []
          liss1 = {}
          liss1 = defaultdict(lambda: 0, liss1)
          liss2 = {}
          sum1 = []
          sum2 = []
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
              rows, msg =  expmodel.search1exp(pdate, session['username'])
              cost = 0
              for row in rows:
                catc = str(row["Category"])
                liss1[catc] = int(liss1[catc]) + int(row['Price'])  
                cost = cost + row['Price']
              liss.insert(i, cost)
            j = 0
            for key in liss1.keys():
              sum1.insert(j, key)
              sum2.insert(j, liss1[key])
              j = j+1
            return render_template('cale.html', first=ress[0], last=ress[1]+1, mon=int(m), yr=int(y), dy=datetime.datetime.now().day, liss = liss, sum1 = sum1, sum2 = sum2, ind=j)
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
              rows, msg =  expmodel.search1exp(pdate, session['username'])
              cost = 0
              for row in rows:
                catc = str(row["Category"])
                liss1[catc] = int(liss1[catc]) + int(row['Price'])  
                cost = cost + row['Price']
              liss.insert(i, cost)
              j = 0
            for key in liss1.keys():
              sum1.insert(j, key)
              sum2.insert(j, liss1[key])
              j = j+1
            return render_template('cale.html', first=ress[0], last=ress[1]+1, mon=int(m), yr=int(y), dy=datetime.datetime.now().day, liss = liss, sum1 = sum1, sum2 = sum2, ind=j)

@app.route('/calexps/<int:d>')
@app.route('/calexps/<int:d>/<int:m>')
@app.route('/calexps/<int:d>/<int:m>/<int:y>')
def calexps(d, m=None, y=None):
    if 'username' not in session:
      return redirect('/')
    else:
      if d < 10:
        d = str(0) + str(d)
      if m < 10:
        m = str(0) + str(m)
      pdate = str(y)+'-'+str(m)+'-'+str(d) 
      rows, msg =  expmodel.search1exp(pdate, session['username'])
      return render_template('allexp.html', rows = rows, message=msg)


@app.route('/editrec_exp',methods = ['POST', 'GET'])
def editrec_exp():
    if 'username' not in session:
        return redirect('/')
    else:   
        if request.method == 'POST':
            res, msg, tday = expmodel.edit_exp(request, session['username'])
            return render_template("expresult.html", result=res, message=msg, tday=tday)
        else:
           return render_template("addexp.html", row={})

@app.route("/edit_exp/<user>")
def edit_exp(user):
  if 'username' in session:
    row, msg = expmodel.editor(user)
    return render_template('addexp.html', row = row)
  return redirect('/')


@app.route('/addexp')
def reg_exp():
   if 'username' not in session:
        return redirect('/')
   return render_template('addexp.html', row={})

@app.route('/exp_disp')
def expdisp():
    if 'username' not in session:
        return redirect('/')
    else:
        rows,msg = expmodel.get_exps(session['username'])
        return render_template('expdisp.html', rows = rows, message=msg)

@app.route("/del_exp/<user>")
def del_exp(user):
  if 'username' in session:
    msg1 = expmodel.deleter(user)
    rows,msg = expmodel.get_exps(session['username'])
    return render_template('expdisp.html', rows = rows, message=msg)
  return redirect('/')

@app.route('/allexp')
def allexp():
   if 'username' not in session:
        return redirect('/')      
   rows,msg = expmodel.get_exps(session['username'])
   return render_template('expdisp.html', rows = rows, message=msg)

@app.route('/addrec_exp',methods = ['POST', 'GET'])
def addrec_exp():
    if 'username' not in session:
        return redirect('/')      
    else:
        if request.method == 'POST':
          res, msg, pday = expmodel.add_exp(request,session['username'])
          return render_template("expresult.html", result=res, message=msg, pday=pday)
        else:
          return render_template("addexp.html", row={})
          
@app.route('/expsearch',methods = ['POST', 'GET'])
def search_exp():
    if 'username' not in session:
        return redirect('/')
    else:   
        if request.method == 'POST':
           res,msg = expmodel.searchexp(request, session['username'])
           return render_template("expdisp.html", rows=res, message=msg)
        else:
           rows, msg = expmodel.get_exps(session['username'])
           return render_template("expdisp.html", rows=rows)
