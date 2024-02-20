import hashlib

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text, Enum, Float, Boolean, BigInteger
from sqlalchemy.orm import relationship
from database import session
from view.management import ManagementMenu

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_lastname = Column(String(45))
    department = Column(Enum('COM', 'GES', 'SUP'))
    password = Column(String(45))
    email = Column(String(45))

    customer = relationship('Customer', back_populates='sales')
    contract = relationship('Contract', back_populates='sales')
    event = relationship('Event', back_populates='support')

    @classmethod
    def create_user(cls):
        print("\n-----NOUVEAU COLLABORATEUR-----")
        name_lastname = input("Nom et prénom: ")
        print("\n-----LES DEPARTEMENTS A RESEIGNER:-----")
        print("-----COM: COMMERCIAL-----")
        print("-----GES: GESTION-----")
        print("-----SUP: SUPPORT-----")
        while True:
            department = input("Departement: ").upper()
            if department in ('COM', 'GES', 'SUP'):
                break
            else:
                print("Département invalide. Veuillez choisir parmi 'COM', 'GES' ou 'SUP'.")
        password = input("Mot de passe: ")
        email = input("Email: ")

        new_user = cls(name_lastname=name_lastname, department=department,
                       password=hashlib.sha256(password).hexdigest(), email=email)

        session.add(new_user)
        session.commit()
        print(f"Le collaborateur {name_lastname} a bien été crée.")
        ManagementMenu.management_users_menu()

    @classmethod
    def delete_user(cls):
        print("Quel collaborateur souhaitez-vous supprimer?")
        id = input("ID du collaborateur: ")

        user = session.query(User).filter(User.id == id).get(1)
        if user:
            while True:
                print(f"Êtes-vous sûr de vouloir effacer le collaborateur {user.name_lastname}?")
                response = input("Oui ou Non?").strip().lower()

                if response == "oui":
                    session.delete(user)
                    session.commit()
                    print(f"{user.name_lastname} a bien été supprimée de la base de données.")
                    ManagementMenu.management_users_menu()
                    break

                elif response == "non":
                    print("Suppression annulée. Vous allez être redirigé vers le menu des collaborateurs.")
                    ManagementMenu.management_users_menu()
                    break

                else:
                    print("Erreur de frappe. Veuillez répondre par 'Oui' ou 'Non'.")

        if user is None:
            print("Erreur de frappe ou aucun collaborateur ne correspond a cette ID, veuillez réeseyer.")
            ManagementMenu.management_users_menu()


class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name_lastname = Column(String(45), ForeignKey('customers.name_lastname'))
    customer_email = Column(String(45), ForeignKey('customers.email'))
    customer_phone = Column(BigInteger, ForeignKey('customers.phone'))
    total_amount = Column(Float, default=0)
    settled_amount = Column(Float, default=0)
    remaining_amount = Column(Float, default=0)
    creation_date = Column(DateTime, default=func.now())
    contract_sign = Column(Boolean, default=False)
    sales_contact_contract = Column(String(45), ForeignKey('customers.sales_contact'))

    sales = relationship('User', back_populates='contract')
    customer = relationship('Customer', back_populates='contract')
    event = relationship('Event', back_populates='contract')

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    contract_id = Column(Integer, ForeignKey('contracts.id'))
    customer_name_lastname = Column(Integer, ForeignKey('contracts.id'))
    customer_email = Column(String(45), ForeignKey('contracts.email'))
    customer_phone = Column(BigInteger, ForeignKey('contracts.phone'))
    title = Column(String(45))
    date_hour_start = Column(DateTime)
    date_hour_end = Column(DateTime)
    adress = Column(String(45))
    guests = Column(Integer, default=0)
    notes = Column(Text)
    support_contact = Column(String(45), ForeignKey('users.name_lastname'))

    support = relationship('User', back_populates='event')
    contract = relationship('Contract', back_populates='event')
