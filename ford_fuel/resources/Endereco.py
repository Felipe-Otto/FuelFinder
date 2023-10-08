from flask_restful import Resource, reqparse
from flask import Flask, request
from resources.utils import construtor_url
from web_scraping import pesquisar_nome_posto

class Endereco(Resource):
    def post(self):
        data = request.get_json()
        rua = data.get('rua', '')
        bairro = data.get('bairro', '')
        cidade = data.get('cidade', '')
        estado = data.get('estado', '')
        cep = data.get('cep', '')
        latitude = data.get('latitude', '')
        longitude = data.get('longitude', '')
        coordenadas = f'/@{latitude},{longitude}'
        endereco = f"{rua} - {bairro}, {cidade} - {estado}, {cep}"
        url = construtor_url(endereco, coordenadas)
        nome_posto = pesquisar_nome_posto(url, cep)
        return {'Nome Posto': nome_posto}

    def get(self):
        # Agora você pode acessar os parâmetros de consulta da URL
        rua = request.args.get('rua', '')
        bairro = request.args.get('bairro', '')
        cidade = request.args.get('cidade', '')
        estado = request.args.get('estado', '')
        cep = request.args.get('cep', '')
        latitude = request.args.get('latitude', '')
        longitude = request.args.get('longitude', '')
        coordenadas = f'/@{latitude},{longitude}'
        endereco = f"{rua} - {bairro}, {cidade} - {estado}, {cep}"
        url = construtor_url(endereco, coordenadas)
        nome_posto = pesquisar_nome_posto(url, cep)
        return {'Nome Posto': nome_posto}
