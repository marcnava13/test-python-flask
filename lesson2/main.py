from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_wtf import CsrfProtect
from modules.forms import loginForm

app = Flask( __name__ )
app.secret_key = 'YOUR_SECRET_KEY' # os.get('SECRET_KEY')
csrf = CsrfProtect(app)

@app.route('/', methods = [ 'GET' ])
def index():
    return render_template( 'layout/homepage.html' )

@app.route('/login', methods = [ 'GET', 'POST' ])
def login():
    login_form = loginForm.LoginForm()
    if login_form.validate_on_submit():
        return redirect('/')
    return render_template( 'layout/login.html', form = login_form, actionForm = '/login' )

if __name__ == '__main__':
    app.run( debug = True, port = 8000 )