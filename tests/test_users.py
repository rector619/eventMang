import pytest
import db
from routers.users.models import User

#Find a way to change the keyspace sp you dont affect production data 

@pytest.fixture(scope='module')
def setup():
    session = db.get_session()
    yield session
    # email='test3@test.com'
    # partition_key_value = User.get(email=email).user_id
    # q = User.objects.filter(email=email, user_id=partition_key_value).allow_filtering()
    q = User.objects.filter(email='test4@test.com')
    if q.count() != 0:
        q.delete()
    session.shutdown()

def test_create_user(setup):
    User.create_user(email='test4@test.com', password='abc123')

def test_duplicate_user(setup):
    with pytest.raises(Exception):
        User.create_user(email='test4@test.com', password='abc123dafd')

def test_invalid_email(setup):
    with pytest.raises(Exception):
        User.create_user(email='test4@test.com', password='abc123dafd') 
    
def test_valid_password(setup):
    # email='test3@test.com'
    # partition_key_value = User.get(email=email).user_id
    # q = User.objects.filter(email=email, user_id=partition_key_value).allow_filtering()
    q = User.objects.filter(email='test4@test.com')
    assert q.count() == 1
    user_obj = q.first()
    assert user_obj.verify_password('abc123') == True
    assert user_obj.verify_password('abc1234') == False

# def test_assert():
#     assert True is True

# def test_equal():
#     assert 1 == 1

# def test_equal():
#     assert 1 != 1

# def test_invalid_assert():
#     with pytest.raises(AssertionError):
#         assert True is not True