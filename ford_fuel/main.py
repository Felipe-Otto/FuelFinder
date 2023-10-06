from flask import Flask
from flask_restful import Api
from resources.Endereco import Endereco

app = Flask(__name__)
api = Api(app)


api.add_resource(Endereco, '/fordfuel')

if __name__ == '__main__':
    app.run(debug=True)
