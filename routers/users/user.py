from typing import List
from fastapi import APIRouter
from uuid import UUID

# from schema import UserBase, UserDisplay
from . import schema, auth
from database import user_db_crud

router = APIRouter(
    prefix='/Accounts',
    tags=['Accounts']
)

#Register  user
@router.post('/RegisterUser', response_model=schema.UserSignupResponseSchema)
def create_user(userData: schema.UserSignupRequestSchema):
    return user_db_crud.create_user("user created successfully" , userData)

# @router.get('/GetAllUsers')
@router.get('/GetAllUsers', response_model=List[schema.UserSignupResponseSchema])
def get_all_users():
    users = user_db_crud.get_all_users()
    return users

@router.delete('/DeleteUser/{id}')
def delete_user_by_id(id: UUID):
    return user_db_crud.delete_user(id)

@router.post('/login', response_model=schema.UserLoginRequestSchema)
def login_user(userData: schema.UserLoginRequestSchema):
    print(userData)
    
    return auth.authenticate(userData)