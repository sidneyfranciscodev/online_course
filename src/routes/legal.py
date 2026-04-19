from fastapi import Request
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.config import TEMPLATES_DIR

router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get(
    "/termos-e-condicoes",
    name='app_terms',
    response_class=HTMLResponse
)
def home(request: Request):
    return templates.TemplateResponse(
        name='pages/legal/terms.html',
        request=request
    )


@router.get(
    "/politica-de-privacidade",
    name='app_privacy',
    response_class=HTMLResponse
)
def services(request: Request):
    return templates.TemplateResponse(
        name='pages/legal/privacy.html',
        request=request
    )

@router.get(
     "/politica-de-cookies",
    name='app_cookies',
    response_class=HTMLResponse
)
def cookies(request: Request):
    return templates.TemplateResponse(
        name='pages/legal/cookies.html',
        request=request
    )