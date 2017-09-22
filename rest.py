from flask import Flask, request
from flask_restful import Resource, Api
from flask.ext.jsonpify import jsonify


app = Flask(__name__)
api = Api(app)


class Test(Resource):
    def get(self):
        data = {"user2_proximity": 3, "Wifi_1": -80, "Wifi_2": -40, "Wifi_3": -40,
                "thermostat": 18, "light": 0, "hour_of_day": 0, "user3_proximity": 3,
                "user1_proximity": 1, "day_of_week": 1, "security": 0, "minute_of_hour": 9,
                "Act_1": 1, "Act_2": 0, "Act_3": 0}

        return jsonify(data)


api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(port='5002')