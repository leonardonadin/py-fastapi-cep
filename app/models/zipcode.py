from sqlalchemy import Column, Integer, String

from app.core.database import Base


class ZipCode(Base):
    __tablename__ = "zipcodes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    address = Column(String)
    number = Column(String)
    neighborhood = Column(String)
    complement = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    ibge_code = Column(String)
    gia = Column(String)
    ddd = Column(String)