from flask                                      import Blueprint, request, jsonify
from flask.restx                                import Namespace, Resource
from radix_challenge.model.facade.sensor_facade import SensorFacade as sensor_f
from api_model                                  import *
from radix_challenge.util.utils                 import *

# --------------- NAMES ---------- >>
api = Namespace(name = 'SensorData', description = 'rota para ler, carregar e deletar dados dos sensores.', path='/')

# --------------- MODELS ---------- >>
model_upload_sensor_data = api.model('model_upload_sensor_data', MODEL_UPLOAD_SENSOR_DATA)

# --------------- ROUTES ---------- >>
@api.route('/insert-sensor-data')
class UploadSensorData(Resource):
    @api.expect(model_upload_sensor_data, validade = True)
    def post(self):
        try:
            result = sensor_f.upload_sensor_data(request.get_json())
            return jsonify(get_dict_endpoint("Sucesso", "dados carregados com sucesso", result))
        except Exception as erro:
            return jsonify(get_dict_endpoint("Erro", "falha no carregamento dos dados", erro)), 400

@api.route('/upload-csv')
class UploadSensorDataCSV(Resource):
    def post(self):
        file = request.files['file']
        df = pd.read_csv(file)
        for row in df.iterrows():
            try:
                equipment_id = row['equipmentId']
                timestamp = row['timestamp']
                value = row['value']
                data = convert_csv_to_dict(equipment_id,timestamp,value)
                result = sensor_f.upload_sensor_data(data)
                return jsonify(get_dict_endpoint("Sucesso", "dados carregados com sucesso", result))
            
            except Exception as erro:
                return jsonify(get_dict_endpoint("Erro", "falha no carregamento dos dados", erro)), 400

@api.route('/get-avg-sensor-data-day')
class GetAvgSensorData(Resource):
    def get(self):
        try:
            result = sensor_f.get_avg_sensor_day()
            return jsonify(get_dict_endpoint("Sucesso", "dados retornados com sucesso", result))
        except Exception as erro:
            return jsonify(get_dict_endpoint("Erro", "falha no retorno dos dados", erro)), 400
@api.route('/get-avg-sensor-data-two-days')
class GetAvgSensorData(Resource):
    def get(self):
        try:
            result = sensor_f.get_avg_sensor_twodays()
            return jsonify(get_dict_endpoint("Sucesso", "dados retornados com sucesso", result))
        except Exception as erro:
            return jsonify(get_dict_endpoint("Erro", "falha no retorno dos dados", erro)), 400
@api.route('/get-avg-sensor-data-week')
class GetAvgSensorData(Resource):
    def get(self):
        try:
            result = sensor_f.get_avg_sensor_week()
            return jsonify(get_dict_endpoint("Sucesso", "dados retornados com sucesso", result))
        except Exception as erro:
            return jsonify(get_dict_endpoint("Erro", "falha no retorno dos dados", erro)), 400
@api.route('/get-avg-sensor-data-month')
class GetAvgSensorData(Resource):
    def get(self):
        try:
            result = sensor_f.get_avg_sensor_month()
            return jsonify(get_dict_endpoint("Sucesso", "dados retornados com sucesso", result))
        except Exception as erro:
            return jsonify(get_dict_endpoint("Erro", "falha no retorno dos dados", erro)), 400
