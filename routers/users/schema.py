from pydantic import BaseModel, SecretStr, validator
from typing import Optional
from uuid import UUID
from .models import User
class UserSignupRequestSchema(BaseModel):
    username: str
    firstname: str
    lastname: str
    email: str
    password: str
    password_confirm: str
    referrer: str


class UserSignupResponseSchema(BaseModel):
    user_id: UUID
    # username: str
    # firstname: str
    # lastname: str
    # email: str 
    # referrer: str 
    username: Optional[str] 
    firstname: Optional[str] 
    lastname: Optional[str] 
    email: Optional[str] 
    referrer: Optional[str] 
    
class UserLoginRequestSchema(BaseModel):
    email: Optional[str]
    username: Optional[str]
    password: str