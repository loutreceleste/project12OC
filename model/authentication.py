import hashlib
import secrets
import datetime
import jwt

from sqlalchemy import and_
from database import session
from model.management import User


def create_jwt(user):

    secret_key = secrets.token_hex(32)
    print(secret_key)

    payload = {
        "id": user.id,
        "name_lastname": user.name_lastname,
        "department": user.department,
        "email": user.email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=2)
    }

    encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256")

    user.secret_key = hashlib.sha256(secret_key.encode()).hexdigest()
    print(user.secret_key)

    user.token = encoded_jwt
    session.commit()

    return encoded_jwt

def check_user(name_lastname, password):
    user = session.query(User).filter(
        and_(
            User.name_lastname == name_lastname,
            User.password == password,
        )
    ).limit(1).first()
    return user

def check_token(token):
    user = session.query(User).filter(User.token == token).first()
    return user

def decode_tonken(token, user):
    print(user.secret_key)
    decrypted_secret_key = hashlib.sha256(user.secret_key.encode()).hexdigest()
    print(decrypted_secret_key)
    decoded_jwt = jwt.decode(token, decrypted_secret_key, algorithms=["HS256"])
    return decoded_jwt
