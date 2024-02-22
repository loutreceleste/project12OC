import secrets

import jwt
from sqlalchemy import and_

from database import session
from model.management import User
from view.authentification import MenuAuthentification

def create_jwt():
        print("\n-----CREATION TOKEN D'AUTHENTIFICATION-----")
        name_lastname = input("Votre Nom et Prenom de votre compte: ")
        password = input("Votre mot de passe: ")

        user = session.query(User).filter(
            and_(
                User.name_lastname == name_lastname,
                User.password == password,
            ).get(1))
        if user:
            payload = {"id": user.id, "name_lastname": user.name_lastname, "department": user.department,
                       "email": user.email}
            secret_key = secrets.token_hex(32)
            encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256")
            print("Veuillez enregistrer votre token, assurez-vous de stocker vos jetons en toute sécurité et de ne "
                  "jamais les divulguer à des tiers non autorisés.")
            print(encoded_jwt)
            MenuAuthentification.main_authentification_menu()
        if user is None:
            print("Identifiant ou mot de passe incorrect, vous allez être redirigée vers le Menu Authentifiaction.")
            MenuAuthentification.main_authentification_menu()
