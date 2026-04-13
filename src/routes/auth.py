from fastapi import Request, Depends
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import src.core.firebase_auth as auth

from config.config import TEMPLATES_DIR

router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("/auth/login", name='app_login', response_class=HTMLResponse)
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

@router.get("/auth/registar", name='app_register', response_class=HTMLResponse)
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


# Still reviewing the user creation process, as it may be better to handle it on the client side using Firebase SDKs, which provide a more seamless experience and better error handling for user registration.
# @router.post("/auth/user/create")
# def create_user(user: dict) -> JSONResponse:
#    auth.create_user(email=user.email, password=user.password)
    
#    return RedirectResponse(url="/auth/login", status_code=302)