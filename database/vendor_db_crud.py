from routers.vendors.models import VendorOrBusiness
from fastapi import HTTPException, status
# from routers.users.models import User
# from . import validators
from routers.vendors import schema
from . import security, validators
from uuid import UUID


#  Create Business/ Vendor
def create_business_vendor(request: schema.RegisterVendorOrBusinessRequestSchema):
        vendorOrBusiness = VendorOrBusiness.objects.filter(request.email == VendorOrBusiness.email).allow_filtering()
        if vendorOrBusiness.count() != 0:
          
            
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"Email is {request.email} not available!")
        valid, msg, request.email = validators._validate_email(request.email)
        
        vendorOrBusiness = VendorOrBusiness.objects.filter(request.phoneNumber == VendorOrBusiness.phoneNumber).allow_filtering()
        if vendorOrBusiness.count() != 0:
           
            
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"Phone number is {request.phoneNumber} not available!")
        valid, msg, request.phoneNumber = validators._validate_phoneNumber(request.phoneNumber)
        
        vendorOrBusiness = VendorOrBusiness.objects.filter(request.businessName == VendorOrBusiness.businessName).allow_filtering()
        if vendorOrBusiness.count() != 0:
      
            
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"Business name is {request.businessName} not available!")
        valid, msg, request.businessName = validators._validate_businessName(request.businessName)
        
        if vendorOrBusiness.count() == 0 and request.confirmPassword != request.password:  
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"Passwords do not match!")
        if not valid:
         
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Invalid email:{msg  }")
            
        obj = VendorOrBusiness(
            firstName = request.firstName, 
            lastName = request.lastName,
            email = request.email,
            businessName = request.businessName,
            businessAddress = request.businessAddress,
            phoneNumber = request.phoneNumber,
            password = request.password,
            confirmPassword = request.confirmPassword,
            hasExistingUserAccount = request.hasExistingUserAccount,
            referrer = request.referrer,
            businessType = request.businessType.value,
            isItARegisteredBusiness = request.isItARegisteredBusiness,
            tinNumber = request.tinNumber,
            rcNumber = request.rcNumber,
            accountNumber = request.accountNumber,
            bankName = request.bankName
        )
        
        obj.save()
        raise HTTPException(status_code=status.HTTP_201_CREATED,
                                detail=f"Successfully created vendor or business!")
    
    
    
#  Get all Business/ Vendor
def get_all_vendors_or_businesses():
    vendorOrBusineses = VendorOrBusiness.objects.all()
    if not vendorOrBusineses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No vendorOrBusiness exists")
        
    response_vendorOrBusinesses = [
        schema.RegisterVendorOrBusinessResponseSchema(
            firstName = vendorOrBusiness.firstName, 
            lastName = vendorOrBusiness.lastName,
            email = vendorOrBusiness.email,
            businessName = vendorOrBusiness.businessName,
            businessAddress = vendorOrBusiness.businessAddress,
            phoneNumber = vendorOrBusiness.phoneNumber,
            password = vendorOrBusiness.password,
            confirmPassword = vendorOrBusiness.confirmPassword,
            hasExistingUserAccount = vendorOrBusiness.hasExistingUserAccount,
            referrer = vendorOrBusiness.referrer,
            businessType = vendorOrBusiness.businessType,
            isItARegisteredBusiness = vendorOrBusiness.isItARegisteredBusiness,
            tinNumber = vendorOrBusiness.tinNumber,
            rcNumber = vendorOrBusiness.rcNumber,
            accountNumber = vendorOrBusiness.accountNumber,
            bankName = vendorOrBusiness.bankName
            )
        for vendorOrBusiness in vendorOrBusineses
        ]
    return response_vendorOrBusinesses
        
        
    
        