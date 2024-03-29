from fastapi import APIRouter

from app.services.zipcode_service import ZipcodeService


router = APIRouter(
    prefix="/zipcode",
    tags=["zipcode"]
)

@router.get("/{zipcode}", tags=["zipcode"])
async def read_zipcode(zipcode: int):
    return ZipcodeService().get_address(zipcode)