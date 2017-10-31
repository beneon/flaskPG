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
    return render_template('user.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)
