import datetime
import jwt

from cryptography.fernet import Fernet
from sqlalchemy import and_
from database import session
from model.principal import User


def create_jwt(user):
    secret_key_bytes = Fernet.generate_key()

    payload = {
        "id": user.id,
        "name_lastname": user.name_lastname,
        "department": user.department,
        "email": user.email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=2)
    }

    encoded_jwt = jwt.encode(payload, secret_key_bytes, algorithm="HS256")

    user.secret_key = secret_key_bytes.decode('utf-8')
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


def decode_token(token, user):
    secret_key_bytes = user.secret_key.encode('utf-8')
    decoded_jwt = jwt.decode(token, secret_key_bytes, algorithms=["HS256"])
    return decoded_jwt
