from flask import Flask
app = Flask(__name__)


@app.route('/')
def Helloworld():
    return '<h1>Hello world Welcome to Heroku !!!</h1>'


@app.route('/welcome')
def Welcome():
    return '<h1>Welcome to My world !!! </h1>'

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)