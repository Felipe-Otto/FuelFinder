from flask import Flask
from flask_restful import Api
from resources.Endereco import Endereco

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)


api.add_resource(Endereco, '/fordfuel')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
