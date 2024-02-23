import hashlib
import secrets
import datetime

import jwt
from sqlalchemy import and_

from database import session
from model.management import User
from view.authentification import MenuAuthentification

def create_jwt():
    print("\n-----CREATION D'UN TOKEN D'AUTHENTIFICATION-----")
    print("Attention, toute création de token engendrera un écrasement de l'ancien!")
    name_lastname = input("Votre Nom et Prenom de votre compte: ")
    password = input("Votre mot de passe: ")

    user = session.query(User).filter(
        and_(
            User.name_lastname == name_lastname,
            User.password == password,
        ).get(1))

    if user:
        payload = {"id": user.id, "name_lastname": user.name_lastname, "department": user.department,
                   "email": user.email, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=2)}
        secret_key = secrets.token_hex(32)
        encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256")

        user.token = encoded_jwt
        user.secret_key = hashlib.sha256(secret_key.encode()).hexdigest()

        session.commit()
        print("Veuillez enregistrer votre token, assurez-vous de stocker vos jetons en toute sécurité et de ne "
              "jamais les divulguer à des tiers non autorisés.")
        print("Ce token expirera dans 2 jours à compter de maintenant.")
        print(encoded_jwt)
        MenuAuthentification.main_authentification_menu()

    if user is None:
        print("Identifiant ou mot de passe incorrect, vous allez être redirigée vers le Menu Authentifiaction.")
        MenuAuthentification.main_authentification_menu()


def check_token():
    print("\n-----CONNEXION AVEC VOTRE TOKEN-----")
    token = input("Veuillez insérer votre token: ")

    user = session.query(User).filter(User.token == token).first()
    if user:
        if user.token_exp and user.token_exp < datetime.datetime.utcnow():
            print("Votre token a expiré. Veuillez générer un nouveau token.")
            MenuAuthentification.main_authentification_menu()
            return

        try:
            decoded_jwt = jwt.decode(token, user.secret_key, algorithms=["HS256"])

            if decoded_jwt:
                print("Connexion réussie avec votre token.")
                MenuAuthentification.main_authentification_menu()
                return user.name_lastname, user.department
            else:
                print("Token invalide. Veuillez vérifier votre token et réessayer.")
                MenuAuthentification.main_authentification_menu()
        except jwt.ExpiredSignatureError:
            print("Le token a expiré. Veuillez générer un nouveau token.")
            MenuAuthentification.main_authentification_menu()
        except jwt.InvalidTokenError:
            print("Token invalide. Veuillez vérifier votre token et réessayer.")
            MenuAuthentification.main_authentification_menu()
    else:
        print("Token invalide. Veuillez vérifier votre token et réessayer.")
        MenuAuthentification.main_authentification_menu()
