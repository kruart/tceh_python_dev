from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world!'


@app.route('/test')
def test1():
    return 'testing!'


@app.route('/user/<name>')
def get_user(name: str):
    return 'Hello, {}!'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
