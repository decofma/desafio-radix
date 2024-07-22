from flask import Flask
from flask_cors import CORS

import radix_challenge.view.bp.root_blueprint as root

def create_app():
    app = Flask(__name__)
    
    CORS(app)
    app.config['PROPAGATE_EXCEPTIONS'] = True    
    root.init(app)
    return app
