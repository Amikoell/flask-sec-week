from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return'<h1 style=" color:green;" > Hello Girl... cogan here...'


if __name__ == "__main__":
    app.run(debug=True)


