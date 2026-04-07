from firebase_admin import auth
from fastapi import Request, HTTPException, Depends, Cookie
from typing import Annotated
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import timedelta


security = HTTPBearer()
headers = Annotated[HTTPAuthorizationCredentials, Depends(security)]

def get_token(credentials: headers) -> str:
    if not credentials.credentials:
        raise HTTPException(detail={'error': 'Invalid token'}, status_code=401)

    return credentials.credentials

def verify_token(token: str = Depends(get_token)) -> dict:   
    try:
        verified_token = auth.verify_id_token(token, check_revoked=True)
            
    except auth.InvalidIdTokenError as e:
        raise HTTPException(detail={'error': e.default_message}, status_code=401)
    except auth.ExpiredIdTokenError as e:
        raise HTTPException(detail={'error': e.default_message}, status_code=401)
    except auth.RevokedIdTokenError as e:
        raise HTTPException(detail={'error': e.default_message}, status_code=401)
    except Exception:
        raise HTTPException(detail={'error': 'Unauthorized'}, status_code=401)

    return {
        "token": token,
        "uid": verified_token["uid"],
        "email": verified_token["email"],
        "claims": verified_token
    }


def create_session(token: str) -> str:
    expires_in = timedelta(days=5)

    try:
        session_cookie = auth.create_session_cookie(token, expires_in=expires_in)
    
    except auth.InvalidIdTokenError as e:
        raise HTTPException(detail={'error': e.default_message}, status_code=401)
    except auth.ExpiredIdTokenError as e:
        raise HTTPException(detail={'error': e.default_message}, status_code=401)
    except auth.RevokedIdTokenError as e:
        raise HTTPException(detail={'error': e.default_message}, status_code=401)
    except Exception:
        raise HTTPException(detail={'error': 'Unauthorized'}, status_code=401)

    return session_cookie


def verify_session(cookie: str):
    try:
        verified_cookie = auth.verify_session_cookie(cookie, check_revoked=True)

    except auth.InvalidSessionCookieError:
        raise HTTPException(detail={'error': 'Unauthorized'}, status_code=401)
    except auth.ExpiredSessionCookieError:
        raise HTTPException(detail={'error': 'Unauthorized'}, status_code=401)
    except auth.RevokedSessionCookieError:
        raise HTTPException(detail={'error': 'Unauthorized'}, status_code=401)
    except Exception:
        raise HTTPException(detail={'error': 'Unauthorized'}, status_code=401)

    return verified_cookie


def authenticate(session: str = Cookie(None, alias='__session')):
    if not session:
        raise HTTPException(detail={'error': 'Unauthorized'}, status_code=401)

    verified = verify_session(session)
        
    return verified