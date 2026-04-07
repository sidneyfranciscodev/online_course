from fastapi import Request, Depends
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.core.firebase_auth import authenticate
from config.config import TEMPLATES_DIR


router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get(
    "/admin/dashboard",
    name="admin_dashboard",
    response_class=HTMLResponse
)
def dashboard(
    request: Request,
    #user = Depends(authenticate)
) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/admin/dashboard.html',
        context={'request': request},
        request=request
    )
