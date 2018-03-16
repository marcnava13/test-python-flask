from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/hello')
def hello():
    param = request.args.get('name', 'world')
    return 'hello {}'.format(param)

@app.route('/bye/')
@app.route('/bye/<name>/<int:num>')
def bye(name = 'world', num = 0):
    return 'bye {}, {}'.format(name, num)

if __name__ == '__main__':
    app.run( debug = True, port = 8000 )