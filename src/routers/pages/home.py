from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from src.utils.templates import templates

router = APIRouter()


@router.get('/', response_class=HTMLResponse)
async def get_home_page(request: Request):
    return templates.TemplateResponse('pages/home.html', {'request': request})
