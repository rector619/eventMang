from typing import List
from fastapi import APIRouter
from uuid import UUID

# from schema import UserBase, UserDisplay
from . import schema, auth
from database import  vendor_db_crud


router = APIRouter(
    prefix='/Accounts',
    tags=['Accounts']
)

#Register  user
@router.post('/RegisterVendorOrBusiness', response_model=schema.RegisterVendorOrBusinessResponseSchema)
def create_business_vendor(userData: schema.RegisterVendorOrBusinessRequestSchema):
    return vendor_db_crud.create_business_vendor(userData)

@router.get('/GetAllVendorsOrBusinesses' , response_model=List[schema.RegisterVendorOrBusinessResponseSchema])
def get_all_vendors_or_businesses():
    vendorOrBusinesses = vendor_db_crud.get_all_vendors_or_businesses()
    return vendorOrBusinesses

# # @router.get('/GetAllUsers')
# @router.get('/GetAllUsers', response_model=List[schema.UserSignupResponseSchema])
# def get_all_users():
#     users = user_db_crud.get_all_users()
#     return users

# @router.delete('/DeleteUser/{id}')
# def delete_user_by_id(id: UUID):
#     return user_db_crud.delete_user(id)

@router.post('/VendorOrBusinessLogin', response_model=schema.LoginVendorOrBusinessRequestSchema)
def vendor_business_login (userData: schema.LoginVendorOrBusinessRequestSchema):
    return auth.vendor_business_login(userData)