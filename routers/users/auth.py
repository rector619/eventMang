import datetime
from jose import jwt, ExpiredSignatureError
import config
from .models import User
from fastapi import HTTPException, status
from routers.users import schema

settings = config.get_settings()

def authenticate(request: schema.UserLoginRequestSchema):
# def authenticate(username, email, password):
    try:
        user_obj = User.objects.filter(request.username==User.username, request.email==User.email).allow_filtering().first()
    except Exception as e:
        user_obj = None
    if user_obj and user_obj.verify_password(request.password):
        return user_obj
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Invalid credentials")
        

def login(user_obj, expires=5):
    raw_data = {
        "user_id": f"{user_obj.id}",
        "role": "admin",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires),
    }
    return jwt.encode(raw_data, settings.secret_key, algorithm=settings.jwt_algorithm)

def verify_user_id(token):
    data = {}
    try:
        date = jwt.decode(token, settings.secret_key, algorithm=[settings.jwt_algorithm])
    except ExpiredSignatureError as e:
        print(e)
    except :
        pass
    if 'user_id' not in data:
        return None
    return data