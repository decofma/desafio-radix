from flask                                      import Blueprint, request, jsonify
from flask.restx                                import Namespace, Resource
from radix_challenge.model.facade.sensor_facade import SensorFacade as sensor_f
from api_model                                  import *
from radix_challenge.util.utils                 import *

# --------------- NAMES ---------- >>
api = Namespace(name="Ping", path="/ping", description='Avaliação de Status Code')

# --------------- ROUTES ---------- >>

@api.route('')
class Ping(Resource):
    def get(self):
        retorno = 'Ping'
        return jsonify(retorno)