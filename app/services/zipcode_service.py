from app.repositories.zipcode_repository import ZipcodeRepository
from app.external.viacep import ViaCep

class ZipcodeService:
    def __init__(self):
        pass

    def get_address(self, zipcode):
        zipcode_model = ZipcodeRepository().get_address(zipcode)

        if not zipcode_model:
            viacep_address = ViaCep(zipcode).get_address()

            if 'erro' in viacep_address:
                return None
            
            zipcode_model = ZipcodeRepository().create_address(
                zipcode=viacep_address['cep'],
                address=viacep_address['logradouro'],
                neighborhood=viacep_address['bairro'],
                city=viacep_address['localidade'],
                state=viacep_address['uf'],
                ibge_code=viacep_address['ibge'],
                gia=viacep_address['gia'],
                ddd=viacep_address['ddd']
            )
        
        return zipcode_model