from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
# from ...config import get_settings
from config import get_settings
import uuid
from database import security
from pydantic import BaseModel, Field

    
class VendorOrBusiness(Model):
    __keyspace__ = get_settings().keyspace
    vendor_id = columns.UUID(primary_key=True, default=uuid.uuid1)  
    firstName = columns.Text()
    lastName = columns.Text()
    email = columns.Text() 
    businessName = columns.Text()
    businessAddress = columns.Text()
    phoneNumber = columns.Text()
    password = columns.Text()
    confirmPassword = columns.Text()
    hasExistingUserAccount = columns.Boolean(default=False)
    referrer = columns.Text()
    businessType = columns.Text()
    isItARegisteredBusiness = columns.Boolean()
    tinNumber = columns.Text()
    rcNumber = columns.Text()
    accountNumber = columns.Text()
    bankName = columns.Text()

    # Rest of your model definition
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return f"RegisterVendorOrBusiness(email={self.email}, user_id={self.user_id})"
    
    def verify_password(self, pw_str):
        pw_hash = self.password
        verified, _ = security.verify_hash(pw_hash, pw_str)
        return verified
    
    

# class VendorOrBusinessVerify(Model):
#     businessName: columns.Text()
#     tinNumber: columns.Text()
#     rcNumber: columns.Text()

# class VendorOrBusinessLogin(Model):
#     businessNameOrEmailAddress:columns.Text()
#     password: columns.Text()
#     rememberClient: columns.Boolean()

# class EmailVerificationCode(Model):
#     clientBaseUrl: columns
#     email: columns.Text()
#     verificationParameter: str

# class EmailConfirmationCode(BaseModel):
#     email: columns.Text()
#     token: columns.Text()
    

# class ResetPasswordToken(BaseModel):
#     clientBaseUrl: columns.Text()
#     email: columns.Text()
#     verificationParameter: columns.Text()

# class ResetPasswordWithToken(BaseModel):
#     resetToken: columns.Text()
#     securityAnswer: columns.Text
#     newPassword: columns.Text()
    
    

    