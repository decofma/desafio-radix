from flask_restx import fields

MODEL_UPLOAD_SENSOR_DATA = {
    "equipmentId"   : fields.String(required=True, description='identificador do equipamento'),
    "timestamp"     :  fields.Date(required=True, description='data e hora que o evento ocorreu, incluindo o fuso horário'),
    "value"         :  fields.Number(required=True, description='valor do sensor com a precisão de duas casas decimais'),
}