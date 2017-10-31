from flask import Flask
from flask.ext.script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>hello world</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>hello {0}!</h1>'.format(name)

if __name__ == '__main__':
    manager.run()