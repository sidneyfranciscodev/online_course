from fastapi import Request, Depends
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import src.core.firebase_auth as auth

from config.config import TEMPLATES_DIR

router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("/auth/login", name='app_auth', response_class=HTMLResponse)
def login(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/auth.html',
        context={
            'request': request,
            'mode': 'login',
            'title': 'Iniciar Sessão'
        },
        request=request
    )

@router.get("/auth/cadastrar", response_class=HTMLResponse)
def register(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        name='pages/auth.html',
        context={
            'request': request,
            'mode': 'register',
            'title': 'Criar conta'
        },
        request=request
    )


@router.post("/auth/session")
def session(verified: dict = Depends(auth.verify_token)) -> JSONResponse:
    id_token = verified.get('token')
    cookie = auth.create_session(id_token)

    response = JSONResponse({"status": 200}, status_code=200)
    response.set_cookie(
        key="__session",
        value=cookie,
        httponly=True,
        secure=False,
        samesite="lax"
    )

    return response

@router.post("/auth/logout")
def logout() -> JSONResponse:
    response = JSONResponse({ "status": "logged out" })
    response.delete_cookie("__Session")
    response.delete_cookie("__session")
    response.delete_cookie("__SESSION")

    return response