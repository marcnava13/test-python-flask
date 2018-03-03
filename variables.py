from flask import Flask
from flask import render_template

# app = Flask(__name__, template_folder = 'name_folder' )
app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    age = 28
    my_list = [ 1, 2, 3, 4]
    return render_template('user.html', name = name, age = age, list = my_list)

if __name__ == '__main__':
    app.run( debug = True, port = 8000 )