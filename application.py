from flask import Flask
from flask_restful import Resource,Api,request

app = Flask(__name__)
api = Api(app)

class sigfox(Resource):
   def get(self):
      args = request.args
      return args


api.add_resource(sigfox,'/sigfox')
if __name__ == "__application__":
   app.run()


""" @app.route("/")
def hello():
    return "Hello, Global Access!" """