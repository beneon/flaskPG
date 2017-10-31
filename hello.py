# hello.py
# main script for flasky learning playground
# chapter 3, jinja

# importing
# =================================
from flask import Flask
from flask import render_template

app = Flask(__name__)

# router area
# =================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    values=[1,2,2,3,4,5,4,6,7]
    return render_template('user.html',name=name,values = values)

@app.route('/test/<selector>')
def testVar(selector):
    mydict = dict()
    mydict['a']='t'
    mydict['t']='a'
    mylist = [1,2,3,4,5]
    key = 'a'
    myintvar = int(selector)
    class myobj:
        def somemethod():
            return "test some method"
    return render_template('test.html',mydict=mydict,key=key,mylist=mylist,myintvar=myintvar,myobj=myobj)

if __name__ == '__main__':
    app.run(debug=True)
