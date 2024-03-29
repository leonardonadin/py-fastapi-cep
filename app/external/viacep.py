import requests

class ViaCep:
    def __init__(self, cep):
        self.cep = cep
        self.url = f'https://viacep.com.br/ws/{cep}/json/'

    def get_address(self):
        response = requests.get(self.url)
        return response.json()