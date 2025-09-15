from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1 style="color:red">您好! Flaks!</h1>'

@app.route("/name")
def name():
    return '<h1>Hello! Robert</h1>'

if __name__ == "__main__":
    app.run(debug=True)