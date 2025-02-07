from flask import Flask
from flask_restful import Api

from vinoteca import Vinoteca

# API
from recursos import *

# Inicializa la aplicación Flask
app = Flask(__name__)

# Configura la API
api = Api(app)
api.add_resource(RecursoBodega, '/api/bodegas/<id>')
api.add_resource(RecursoBodegas, '/api/bodegas')
api.add_resource(RecursoCepa, '/api/cepas/<id>')
api.add_resource(RecursoCepas, '/api/cepas')
api.add_resource(RecursoVino, '/api/vinos/<id>')
api.add_resource(RecursoVinos, '/api/vinos')

if __name__ == "__main__":
    Vinoteca.inicializar()
    app.run(debug=False)
