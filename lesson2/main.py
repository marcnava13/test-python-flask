from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from flask import session
from flask_wtf import CsrfProtect
from modules.forms import loginForm

app = Flask( __name__ )
app.secret_key = 'YOUR_SECRET_KEY' # os.get('SECRET_KEY')
csrf = CsrfProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template( '404.html' ), 404

@app.before_request
def before_request():
    print 'before_request'

@app.after_request
def after_request(response):
    print 'after_request'
    return response

@app.route('/', methods = [ 'GET' ])
def index():
    if 'username' in session:
        username = session['username']
        print(username)
    return render_template( 'layout/homepage.html' )

@app.route('/login', methods = [ 'GET', 'POST' ])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    login_form = loginForm.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate_on_submit():
        session['username'] = login_form.email.data
        return redirect(url_for('index'))
    return render_template( 'layout/login.html', form = login_form, actionForm = '/login' )

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run( debug = True, port = 8000 )