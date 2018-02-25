import flask
from flask import render_template
app = flask.Flask(__name__)

@app.route('/')
def page():
  return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
  app.run(host='192.168.1.3',port=5050)

