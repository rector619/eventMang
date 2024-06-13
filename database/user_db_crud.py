from routers.users.models import User
from fastapi import HTTPException, status
from routers.users import schema
from . import security, validators
from uuid import UUID

def set_password(self, pw, commit=False):
        pw_hash = security.generate_hash(pw)
        self.password = pw_hash
        if commit:
            self.save()
        return True
    
# def verify_password(self, pw_str):
#         pw_hash = self.password
#         verified, _ = security.verify_hash(pw_hash, pw_str)
#         return verified

#db create users
# def create_user(email, password=None):
def create_user(request: schema.UserSignupRequestSchema):
     
        user = User.objects.filter(request.email == User.email).allow_filtering()
        if user.count() != 0:
            # return Exception({"User already has an account!"})
            
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"Email is {request.email} not available!")
        valid, msg, request.email = validators._validate_email(request.email)

        if user.count() == 0 and request.password_confirm != request.password:
                 
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"Passwords do not match!")

        if not valid:
            # return Exception(f"Invalid email:{msg  }")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Invalid email:{msg  }")
      
        obj = User(
             username = request.username,
             firstname = request.firstname,
             lastname = request.lastname,
             email = request.email,
             password = request.password,
             referrer = request.referrer
        )
        obj.save()
        return obj 

#db read users
def get_all_users():
    #  print(list(User.objects.all()))
     users = User.objects.all()
     if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"No users exists")
     
      # Convert User objects to UserSignupResponseSchema objects
     response_users = [
        schema.UserSignupResponseSchema(
            user_id=user.user_id,
            username=user.username,
            firstname=user.firstname,
            lastname=user.lastname,
            email=user.email,
            referrer=user.referrer
        )
        for user in users
    ]

     return response_users


#db get user by id
# def get_user(id):
#      user =  

# def get_user_by_username(request: , username : str):
#     user = User.objects.filter(request.username == username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'User with username {username} not found')
#     return user
#db delete user

def delete_user(id: UUID):
      user = User.objects.get(User.user_id == id)
      user.delete()
      if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    
      return 'ok'
  

        
        
              