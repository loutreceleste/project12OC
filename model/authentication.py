import hashlib
import secrets
import datetime

import jwt
from sqlalchemy import and_

from database import session
from model.management import User
from view.authentification import AuthentificationMenu, AuthenticationViews

def create_jwt():
    name_lastname, password = AuthenticationViews.token_creation()

    user = session.query(User).filter(
        and_(
            User.name_lastname == name_lastname,
            User.password == password,
            )
        ).limit(1).first()

    if user:
        payload = {"id": user.id, "name_lastname": user.name_lastname, "department": user.department,
                   "email": user.email, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=2)}
        secret_key = secrets.token_hex(32)
        encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256")

        user.token = encoded_jwt
        user.secret_key = hashlib.sha256(secret_key.encode()).hexdigest()

        session.commit()
        AuthenticationViews.token_print(encoded_jwt)
        AuthentificationMenu.main_authentification_menu()

    else:
        AuthenticationViews.error_authentication()
        AuthentificationMenu.main_authentification_menu()


def check_token():
    token = AuthenticationViews.token_cheking()

    user = session.query(User).filter(User.token == token).limit(1).first()
    if user:
        if user.token_exp and user.token_exp < datetime.datetime.utcnow():
            AuthenticationViews.expiration_date_token()
            AuthentificationMenu.main_authentification_menu()
            return

        try:
            decoded_jwt = jwt.decode(token, user.secret_key, algorithms=["HS256"])

            if decoded_jwt:
                print("Connexion réussie avec votre token.")
                AuthentificationMenu.main_authentification_menu()
                return user.name_lastname, user.department
            else:
                AuthenticationViews.invalid_token()
                AuthentificationMenu.main_authentification_menu()
        except jwt.ExpiredSignatureError:
            AuthenticationViews.expiration_date_token()
            AuthentificationMenu.main_authentification_menu()
        except jwt.InvalidTokenError:
            AuthenticationViews.invalid_token()
            AuthentificationMenu.main_authentification_menu()
    else:
        AuthenticationViews.invalid_token()
        AuthentificationMenu.main_authentification_menu()
