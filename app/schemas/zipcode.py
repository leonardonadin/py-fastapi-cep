from pydantic import BaseModel


class ZipCodeBase(BaseModel):
    code: str
    address: str
    number: str
    neighborhood: str
    complement: str
    city: str
    state: str
    country: str
    ibge_code: str
    gia: str
    ddd: str