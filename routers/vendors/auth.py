import datetime
from jose import jwt, ExpiredSignatureError
import config
from .models import VendorOrBusiness
from routers.users import schema

settings = config.get_settings()

# def authenticate(request: schema.UserLoginRequestSchema):
def authenticate(businessName, email, password):
    try:
        vendorOrBusiness_obj = VendorOrBusiness.objects.allow_filtering.get(businessName=businessName, email=email)
    except Exception as e:
        vendorOrBusiness_obj = None
    if not vendorOrBusiness_obj.verify_password(password):
        return None
    return vendorOrBusiness_obj

def vendor_business_login(vendorOrBusiness_obj, expires=5):
    raw_data = {
        "vendor_id": f"{vendorOrBusiness_obj.id}",
        "role": "admin",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires),
        
    }
    return jwt.encode(raw_data, settings.secret_key, algorithm=settings.jwt_algorithm)

def verify_vendor_id(token):
    data = {}
    try:
        date = jwt.decode(token, settings.secret_key, algorithm=[settings.jwt_algorithm])
    except ExpiredSignatureError as e:
        print(e)
    except :
        pass
    if 'vendor_id' not in data:
        return None
    return data