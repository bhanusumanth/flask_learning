from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")


def index():
    hello_world = "<h1>Hello World!!!</h1>"
    return hello_world