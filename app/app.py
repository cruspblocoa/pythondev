from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'


@app.route('/name/<name>')
def nome(name):
    return jsonify({"name":name})


if __name__ == "__main__":
    app.run()