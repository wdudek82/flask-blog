from project import app


@app.route('/hello/')
def hello_world():
    return 'Hello, World!'


@app.route('/')
def index():
    return 'It works!'
