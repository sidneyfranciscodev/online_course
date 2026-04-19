from fastapi import Request, Depends
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.core.firebase_auth import authenticate
from config.config import TEMPLATES_DIR


router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get(
    "/admin/painel",
    name="admin_dashboard",
    response_class=HTMLResponse
)
def dashboard(
    request: Request,
    #user = Depends(authenticate)
) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/admin/dashboard.html',
        request=request
    )

@router.get(
    "/admin/crud/users",
    name="admin_users",
    response_class=HTMLResponse
)
def users(
    request: Request,
    #user = Depends(authenticate)
) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/admin/crud.html',
        request=request
    )

@router.get(
    "/admin/crud/modules",
    name="admin_modules",
    response_class=HTMLResponse
)
def modules(
    request: Request,
    #user = Depends(authenticate)
) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/admin/crud.html',
        request=request
    )

@router.get(
    "/admin/crud/lessons",
    name="admin_lessons",
    response_class=HTMLResponse
)
def lessons(
    request: Request,
    #user = Depends(authenticate)
) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/admin/crud.html',
        request=request
    )

@router.get(
    "/admin/settings",
    name="admin_settings",
    response_class=HTMLResponse
)
def settings(
    request: Request,
    #user = Depends(authenticate)
) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/admin/settings.html',
        request=request
    )