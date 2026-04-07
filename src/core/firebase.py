import firebase_admin as firebase
from firebase_admin import credentials

import os
import json
from dotenv import load_dotenv

if os.getenv("ENV") != "prod":
    load_dotenv()

path = os.getenv('FIREBASE_CRED')

if not path:
    raise ValueError("FIREBASE_CRED is not set")

config = json.loads(path)

def firebase_init():
    if not firebase._apps:
        cred = credentials.Certificate(config)
        firebase.initialize_app(cred)