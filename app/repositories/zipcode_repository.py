from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db, init_db
from app.models.zipcode import ZipCode

class ZipcodeRepository:

    def __init__(self):
        init_db()


    def get_address(self, zipcode: str):
        db = get_db()
        with db as db_session:
            zipcode_model = (
                db_session.query(ZipCode)
                .filter(ZipCode.code == str(zipcode))
                .first()
            )

        return zipcode_model
    
    def create_address(self, **kwargs):
        db = get_db()
        with db as db_session:
            zipcode = ZipCode()
            zipcode.code = kwargs.get('zipcode').replace('-', '')
            zipcode.address = kwargs.get('address')
            zipcode.neighborhood = kwargs.get('neighborhood')
            zipcode.city = kwargs.get('city')
            zipcode.state = kwargs.get('state')
            zipcode.ibge_code = kwargs.get('ibge_code')
            zipcode.gia = kwargs.get('gia')
            zipcode.ddd = kwargs.get('ddd')

            db_session.add(zipcode)
            db_session.commit()
            db_session.refresh(zipcode)

        return zipcode