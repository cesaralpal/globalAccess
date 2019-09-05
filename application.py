from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
if __name__ == '__application__':
    app.run(host='localhost', port=5000, debug=True)