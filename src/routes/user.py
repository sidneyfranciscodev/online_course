from fastapi import Request, Depends
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.core.firebase_auth import authenticate
from config.config import TEMPLATES_DIR

router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES_DIR)

@router.get(
    "/user/dashboard",
    name="user_dashboard",
    response_class=HTMLResponse
)
def dashboard(
    request: Request,
    #user = Depends(authenticate)
) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/user/dashboard.html',
        request=request
    )

@router.get(
    "/user/{module}",
    name="user_module",
    response_class=HTMLResponse
)
def module(
    request: Request,
    module: str = None,
    #user = Depends(authenticate),
) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/user/module.html',
        context={ 'module': module },
        request=request
    )

@router.get(
    "/user/{module}/{lesson}",
    name="user_lesson",
    response_class=HTMLResponse
)
def lesson(
    request: Request,
    module: str = None,
    lesson: str = None,
    #user = Depends(authenticate),
) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/user/lesson.html',
        context={
            'module': module,
            'lesson': lesson
        },
        request=request
    )