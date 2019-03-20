from flask import Flask,abort,jsonify, request
from flask_restful import Resource, Api

app = app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return({'about':'Hello World - REST'})


    def post(self):
        some_json = request.get_json(force=True)
        return ({'Sent - REST' :some_json},201)


class Multi(Resource):
    def get(self,num):
        return(jsonify({'mult 10' : num * 10}))

api.add_resource(HelloWorld,'/api')

api.add_resource(Multi,'/multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)
