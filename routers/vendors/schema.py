from pydantic import BaseModel, SecretStr, validator
from typing import Optional
from uuid import UUID
from .models import VendorOrBusiness
from enum import Enum


class BusinessType(str, Enum):
    SOLE_PROPRIETORSHIP = "Sole Proprietorship"
    PARTNERSHIP = "Partnership"
    CORPORATION = "Corporation"
    LLC = "Limited Liability Company"
    OTHER = "Other"


class RegisterVendorOrBusinessRequestSchema(BaseModel):
    firstName: str
    lastName: str
    email: str
    businessName: str
    businessAddress: str
    phoneNumber: str
    password: str
    confirmPassword: str
    hasExistingUserAccount: bool
    referrer: str = None
    businessType: BusinessType
    isItARegisteredBusiness: bool
    tinNumber: str = None
    rcNumber: str = None
    accountNumber: str
    bankName: str
    
class RegisterVendorOrBusinessResponseSchema(BaseModel):
    firstName: str
    lastName: str
    email: str
    businessName: str
    businessAddress: str
    phoneNumber: str
    password : str 
    confirmPassword: str
    hasExistingUserAccount: bool
    referrer: str
    businessType: str
    isItARegisteredBusiness: bool
    tinNumber: Optional[str]
    rcNumber: Optional[str]
    accountNumber: str
    bankName: str
    
class LoginVendorOrBusinessRequestSchema(BaseModel):
    businessName: Optional[str]
    email: Optional[str]
    password: str
    rememberClient: Optional[bool]
    
    
    