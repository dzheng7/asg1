from flask import Flask, request
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

#users

class Hello(Resource):
    #args = request.args
    #args = "l"
    def get(self):
        args=request.args
#        try:
#            return "Hello " + args['name'] + "!"
#        except:
#            return "Hello user!"
        arg = "Hello world!"
        return "Hello world!", 200
    def post(self):
        return "",405
#        if args is None
#            return "Hello user!"
#        return "Hello " + args.name + "!"

class Test(Resource):
    #args = request.args
    #args = "l"
    def get(self):
        return "GET request received", 200
    def post(self):
        try:
            return "POST message received: " + request.args['msg'], 200
        except:
            return "POST message received", 200

#api.add_resource(Req, "/user/<string:name>", endpoint=)
api.add_resource(Hello, "/hello", endpoint="") 
#api.add_resource(Hello, "/hello?name=<string:name>", endpoint="hello name")
api.add_resource(Test, "/test", endpoint="")
api.add_resource(Test, "/test?msg=<string:msg>", endpoint="test msg")


#ADD RESOURCES FOR EACH METHOD, CHECK HOW TOERENCIATE BETWEEN GET/POST/PUT FOR THE SAME URL
#if anything's missing, refer to app1.py
#FIGURE OUT WAY TO CHECK RESOURCE TYPE
    #like in the get method, find out how to check if it's hello or check
#also, how to post status codes



#app.run(debug=True)
app.run(host='0.0.0.0', port=8080, debug=True)
