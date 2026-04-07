from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.routes.admin import router as admin
from src.routes.auth import router as auth
from src.routes.legal import router as legal
from src.routes.user import router as user
from src.core.firebase import firebase_init
from config.config import TEMPLATES_DIR, ASSETS_DIR


app = FastAPI()
firebase_init()

app.mount(
    '/assets', 
    StaticFiles(directory=ASSETS_DIR), 
    name='assets'
)

templates = Jinja2Templates(directory=TEMPLATES_DIR)

app.include_router(admin)
app.include_router(auth)
app.include_router(legal)
app.include_router(user)

@app.get('/')
def main():
    return RedirectResponse(url='/auth/login')