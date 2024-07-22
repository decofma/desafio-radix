from flask                                  import Blueprint
from flask_restx                            import Api
from flask.helpers                          import url_for

# --------------- API IMPORT ---------- >>
from ..api.sensor_api                       import api as sensor_api
from ..api.ping_api                         import api as ping_api

# --------------- CONSTANTS  ---------- >>
BLUEPRINT_NAME                              = 'root_bp'
BLUEPRINT_URL                               = '/radix-eng/api/sensor_data'
API_VERSION                                 = '1.0'
API_TITLE                                   = 'Radix Challenge API'
API_DESCRIPTION                             = 'API criada para receber e armazenar os dados lidos dos sensores de empresas do setor de oleo e gas'

# --------------- BLUEPRINT ---------- >>
bp = Blueprint(BLUEPRINT_NAME, __name__, url_prefix=BLUEPRINT_URL)

@property
def specs_url(self):
    if os.environ.get("FLASK_ENV") == "production":
            _scheme = "https"
    else:
            _scheme = "http" 
    return url_for(self.endpoint('specs'), external=True, _scheme=_scheme)

# --------------- API ---------- >>
Api.specs_url = specs_url
api = Api(bp,version = API_VERSION, base_url = BLUEPRINT_URL, title = API_TITLE, description = API_DESCRIPTION)

api.add_namespace(sensor_api)
api.add_namespace(ping_api)

def init_app(app):
    print('Inicialização do Blueprint da API Radix Challenge')
    app.register_blueprint(bp)