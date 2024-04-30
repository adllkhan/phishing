from fastapi import APIRouter
from fastapi.responses import FileResponse

from api.services import generate_report


router = APIRouter(prefix="/report")


@router.get("", response_class=FileResponse)
async def generate(domain: str) -> FileResponse:
    path = generate_report(domain=domain)
    print(path)
    return FileResponse(path=path)
