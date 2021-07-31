# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from random import randint
import json


# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        return jsonify({'message': 'hello world'})

    # Corresponds to POST request
    def post(self):
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201


# another resource to calculate the square of a number
class RandomThousand(Resource):

    def get(self, num=1000):
        return jsonify({'square': randint(1, num)})

    def post(self):
        data = request.get_json()  # status code
        input_data = json.loads(request.get_json())
        s_range = 1
        end_rnage = 1000

        if input_data['start_range'].isnumeric():
            u_start_range = input_data['start_range']

        if input_data['end_range'].isnumeric():
            u_end_range = input_data['end_range']

        if u_start_range < u_end_range:
            s_range = u_start_range
            end_rnage = u_end_range

        return jsonify({'data': randint(s_range, end_rnage)}), 201



# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(RandomThousand, '/square/<int:num>')

# driver function
if __name__ == '__main__':
    app.run(debug=True)
