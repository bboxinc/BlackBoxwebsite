from flask import Flask, session, render_template, request, redirect, g, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def page():
  return render_template('index.html')

@app.route('/login', methods = ['GET','POST'])
def login():
	if request.method == 'POST':
        	session.pop('user', None)
        	if request.form['password'] == 'password':
            		session['user'] = request.form['username']
            		return redirect(url_for('protected'))
	return render_template('login.html')

@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html')

    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped!'


if __name__ == '__main__':
<<<<<<< HEAD
  app.run()
=======
  app.run(host='192.168.1.3',port=5050)

>>>>>>> fbb52f36de445c84b714a1dad851fb68f2129a6d
