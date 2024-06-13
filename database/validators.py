from email_validator import validate_email, EmailNotValidError 

def _validate_email(email):
    msg=""
    valid = False
    try:
        valid = validate_email(email)
        #update the email var with a normalized value
        email = valid.email
        valid = True
    except EmailNotValidError as e:
        msg = str(e)
    return valid, msg, email

def _validate_phoneNumber(phoneNumber):
    msg=""
    valid = False
    if len(phoneNumber) == 11:
        valid = True
    else:
        msg = "Phone number must be 11 digits"
    return valid, msg, phoneNumber

def _validate_businessName(businessName):
    msg=""
    valid = False
    if len(businessName) >= 3:
        valid = True
    else:
        msg = "Business name must be at least 3 characters"
    return valid, msg, businessName


  
# def passwords_match(cls, v, values, **kwargs):
#         password = values.get('password')
#         password_confirm = v
#         if password != password_confirm:
#             raise ValueError("Passwords do not match")
#         return v
