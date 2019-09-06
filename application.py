from flask import Flask
from flask_restful import Resource,Api,request

app = Flask(__name__)
api = Api(app)

class sigfox(Resource):
   def get(self):
      args = request.args
      return args
api.add_resource(sigfox,'/sigfox')

if __name__ == '__application__':
    app.run(host='127.0.0.1', port=8080, debug=True)
""" @app.route("/")
def hello():
    return "Hello, Global Access!" """