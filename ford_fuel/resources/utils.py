import urllib.parse
def construtor_url(endereco, coordenada):
    url = 'https://www.google.com/maps/search/posto+de+gasolina+'
    endereco = endereco.replace(' ', '+')
    url += endereco
    url += coordenada
    return url

def confirmador_posto(enderecos, cep):
    print(enderecos)
    for chave, valor in enderecos.items():
        cep_sup = valor[-9:]
        if cep_sup == cep:
            return chave  # Retorna a chave correspondente ao CEP
    return None



