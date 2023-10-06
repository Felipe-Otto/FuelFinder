import urllib.parse
def construtor_url(endereco, coordenada):
    url = 'https://www.google.com/maps/search/posto+de+gasolina+'
    endereco = endereco.replace(' ', '+')
    print(endereco)
    url += endereco
    url += coordenada
    print(url)
    return url
