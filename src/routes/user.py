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
        context={'request': request},
        request=request
    )

@router.get(
    "/user/{module_id}",
    name="user_module",
    response_class=HTMLResponse
)
def module(
    request: Request,
    #user = Depends(authenticate),
    module_id: str = None
) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/user/module.html',
        context={
            'request': request, 
            'module_id': module_id
        },
        request=request
    )

@router.get(
    "/user/{module_id}/{lesson_id}",
    name="user_lesson",
    response_class=HTMLResponse
)
def lesson(
    request: Request,
    #user = Depends(authenticate),
    module_id: str = None,
    lesson_id: str = None
) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/user/lesson.html',
        context={
            'request': request,
            'module_id': module_id,
            'lesson_id': lesson_id
        },
        request=request
    )