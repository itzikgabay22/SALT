from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import NormalCheck
from DAL import *

class Model(Resource):
    def get(self):
        app.logger.info("Get Request for Models")
        return jsonify(Globals.models_dict)

    def post(self):
        app.logger.info("POST Request for Models")
        json_data = load_josn_from_string(request.data)
        load_models_to_dict(json_data)
        print(json_data)
        return jsonify({"OK": "The Model's Data Indexed Successfully"})



class Default(Resource):
    def get(self):
        app.logger.info("Get Request to Root Page")
        return jsonify({"SALT Ex": "I Hope You Will Like It. Please Navigate to /api/v1/models or /api/v1/normal"})


class Normal(Resource):
    def get(self):
        json_data = load_josn_from_string(request.data)
        errors = NormalCheck.check_request(json_data)
        if len(errors) == 0:
            return jsonify({"Normal" : "All parameters  matching to the model"})
        return jsonify({"Abnormal": errors})


app = Flask(__name__)
api = Api(app)

api.add_resource(Normal, '/api/v1/normal')
api.add_resource(Model, '/api/v1/models')
api.add_resource(Default, '/')


@app.errorhandler(404)
def not_found(e):
    app.logger.error(e)
    return jsonify(error=str(e)), 404






