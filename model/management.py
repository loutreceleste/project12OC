import hashlib
import re

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text, Enum, Float, Boolean, BigInteger
from sqlalchemy.orm import relationship
from database import session

from view.management import ManagementMenu
from view.support import SupportMenu
from view.sales import SalesMenu
from model.sales import Customer

Base = declarative_base()

def check_date_format(date_str):
    pattern = r"^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}$"
    return re.match(pattern, date_str)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_lastname = Column(String(45))
    department = Column(Enum('COM', 'GES', 'SUP'))
    password = Column(String(45))
    email = Column(String(45))
    token = Column(String(300))
    secret_key = Column(String(300))

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
                       password=hashlib.sha256(password.encode()).hexdigest(), email=email)

        session.add(new_user)
        session.commit()
        print(f"Le collaborateur {name_lastname} a bien été crée.")
        ManagementMenu.management_users_menu()

    @classmethod
    def delete_user(cls):
        print("Quel collaborateur souhaitez-vous supprimer?")
        id = input("ID du collaborateur: ")

        user = session.query(User).filter(User.id == id).first()
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
                    print("Suppression annulée. Vous allez être redirigé vers le Menu Collaborateur.")
                    ManagementMenu.management_users_menu()
                    break

                else:
                    print("Erreur de frappe. Veuillez répondre par 'Oui' ou 'Non'.")

        if user is None:
            print("Erreur de frappe ou aucun collaborateur ne correspond a cette ID. Vous allez être redirigé vers le "
                  "Menu Collaborateur.")
            ManagementMenu.management_users_menu()


    @classmethod
    def update_user(cls):
        print("Quel collaborateur souhaitez-vous modifier?")
        id = input("ID du collaborateur: ")

        user = session.query(User).filter(User.id == id).first()
        if user:
            print(f"\n-----MISE A JOUR DU COLLABORATEUR N°{id}-----")
            name_lastname = input(f"Nom et prénom: {user.name_lastname}")
            print("\n-----LES DEPARTEMENTS A RESEIGNER:-----")
            print("-----COM: COMMERCIAL-----")
            print("-----GES: GESTION-----")
            print("-----SUP: SUPPORT-----")
            while True:
                department = input(f"Departement: {user.departement}").upper()
                if department in ('COM', 'GES', 'SUP'):
                    break
                else:
                    print("Département invalide. Veuillez choisir parmi 'COM', 'GES' ou 'SUP'.")
            password = input("Mot de passe (laissez vide pour ne pas modifier): ")
            email = input(f"Email: {user.email}")

            user.name_lastname = name_lastname
            user.departement = department
            if password.strip():
                user.password = hashlib.sha256(password.encode()).hexdigest()
            user.email = email

            session.commit()
            print(f"Le collaborateur {user.name_lastname} a bien ete modifié")
            ManagementMenu.management_users_menu()

        if user is None:
            print("Erreur de frappe ou aucun collaborateur ne correspond a cette ID. Vous allez être redirigé vers le "
                  "Menu Collaborateur.")
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

    @classmethod
    def create_contract(cls):
            print("À partir de quel client souhaitez-vous créer un contrat?")
            id = input("ID du client: ")

            customer = session.query(Customer).filter(Customer.id == id).first()

            if customer:
                print(f"Souhaitez vous créer un contrat pour le client {customer.name_lastname}?")
                response = input("Oui ou Non?").strip().lower()

                if response == "oui":
                    print("\n-----NOUVEAU CONTRAT-----")
                    while True:
                        total_amount = input(f"Cout total du contrat: ")
                        if total_amount.isdigit():
                            total_amount = int(total_amount)
                            break
                        else:
                            print("Veuillez indiquer un nombre entier.")
                    while True:
                        settled_amount = input("Montant déjà réglé: ")
                        if settled_amount.isdigit():
                            settled_amount = int(settled_amount)
                            break
                        else:
                            print("Veuillez indiquer un nombre entier.")
                    while True:
                        contract_sign = input("Le contrat a-t-il été validé par le client? (Oui=True / Non=False): ")
                        if contract_sign in ('True', 'False'):
                            break
                        else:
                            print('Veuillez répondre par "True" ou par "False"')

                    new_contract = cls(customer_name_lastname=customer.name_lastname, customer_email=customer.email,
                                       customer_phone=customer.phone, total_amount=total_amount,
                                       settled_amount=settled_amount, contract_sign=contract_sign,
                                       sales_contact_contract=customer.sales_contact)

                    session.add(new_contract)
                    session.commit()
                    print("Votre contrat a été créé avec succès!")
                    ManagementMenu.management_contrats_menu()

                if response == "non":
                    print("Création annulée. Vous allez être redirigée vers le Menu Contrat.")
                    ManagementMenu.management_contrats_menu()

            if customer is None:
                print("Erreur de frappe ou aucun client ne correspond a cette ID. Vous allez être redirigé vers le "
                  "Menu Contrat.")
                ManagementMenu.management_contrats_menu()

    @classmethod
    def update_contract(cls):
        print("Quel contrat souhaitez-vous modifier?")
        id = input("ID du contrat: ")

        contract = session.query(Contract).filter(Contract.id == id).first()

        if contract:
            print(f"Souhaitez-vous conserver le client n°{contract.id} associé à cet événement?")
            response = input("Oui ou Non").strip().lower()
            if response == "oui":
                print(f"\n-----MISE A JOUR DU CONTRAT N°{id}-----")
                while True:
                    total_amount = input(f"Cout total du contrat: {contract.contract_total_amount}")
                    if total_amount.isdigit():
                        total_amount = int(total_amount)
                        break
                    else:
                        print("Veuillez indiquer un nombre entier.")
                while True:
                    settled_amount = input(f"Montant déjà réglé: {contract.settled_amount}")
                    if settled_amount.isdigit():
                        settled_amount = int(settled_amount)
                        break
                    else:
                        print("Veuillez indiquer un nombre entier.")
                while True:
                    contract_sign = input("Le contrat a-t-il été validé par le client? (Oui=True / Non=False): "
                                          f"{contract.contract_sign}")
                    if contract_sign in ('True', 'False'):
                        break
                    else:
                        print('Veuillez répondre par "True" ou par "False"')

                contract.total_amount = total_amount
                contract.settled_amount = settled_amount
                contract.contract_sign = contract_sign

                session.commit()
                print("Le contrat a été correctement modifié!")
                ManagementMenu.management_contrats_menu()

        if contract is None:
            print("Erreur de frappe ou aucun contrat ne correspond a cette ID. Vous allez être redirigé vers le "
                  "Menu Contrat.")
            ManagementMenu.management_contrats_menu()

    @classmethod
    def update_contract_sales(cls, user):
        print("Quel contrat souhaitez-vous modifier?")
        id = input("ID du contrat: ")

        contract = session.query(Contract).filter(Contract.id == id).first()

        if contract.sales_contact_contract == user.name_lastname:
            if contract:
                print(f"Souhaitez-vous conserver le client n°{contract.id} associé à cet événement?")
                response = input("Oui ou Non").strip().lower()
                if response == "oui":
                    print(f"\n-----MISE A JOUR DU CONTRAT N°{id}-----")
                    while True:
                        total_amount = input(f"Cout total du contrat: {contract.contract_total_amount}")
                        if total_amount.isdigit():
                            total_amount = int(total_amount)
                            break
                        else:
                            print("Veuillez indiquer un nombre entier.")
                    while True:
                        settled_amount = input(f"Montant déjà réglé: {contract.settled_amount}")
                        if settled_amount.isdigit():
                            settled_amount = int(settled_amount)
                            break
                        else:
                            print("Veuillez indiquer un nombre entier.")
                    while True:
                        contract_sign = input("Le contrat a-t-il été validé par le client? (Oui=True / Non=False): "
                                              f"{contract.contract_sign}")
                        if contract_sign in ('True', 'False'):
                            break
                        else:
                            print('Veuillez répondre par "True" ou par "False"')

                    contract.total_amount = total_amount
                    contract.settled_amount = settled_amount
                    contract.contract_sign = contract_sign

                    session.commit()
                    print("Le contrat a été correctement modifié!")
                    SalesMenu.sale_contracts_menu()

            if contract is None:
                print("Erreur de frappe ou aucun contrat ne correspond a cette ID. Vous allez être redirigé vers le "
                      "Menu Contrat.")
                SalesMenu.sale_contracts_menu()

        else:
            print("Vous n'êtes pas en change de ce contrat. Vous allez être redirigé vers le Menu Contrat.")
            SalesMenu.sale_contracts_menu()

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

    @classmethod
    def create_event(cls):
        print("À partir de quel contrat souhaitez-vous créer un événement?")
        id = input("ID du contrat: ")

        contrat = session.query(Contract).filter(Contract.id == id).first()

        if contrat:
            if contrat.contract_sign:
                print(f"Souhaitez vous créer un événement pour le client {contrat.customer_name_lastname} à partir du "
                      f"contrat n°{contrat.id}?")
                response = input("Oui ou Non?: ").strip().lower()

                if response == "oui":
                    print("\n-----NOUVEL EVENEMENT-----")
                    title = input(f"Nom de l'événement: ")
                    while True:
                        date_hour_start = input(f"Date et heure du début de l'événement (format AAAA/MM/JJ HH:MM:SS): ")
                        if check_date_format(date_hour_start):
                            break
                        else:
                            print("Format invalide. Veuillez saisir la date et l'heure au format AAAA/MM/JJ HH:MM:SS.")
                    while True:
                        date_hour_end = input(f"Date et heure de fin de l'événement (format AAAA/MM/JJ HH:MM:SS): ")
                        if check_date_format(date_hour_end):
                            break
                        else:
                            print(
                                "Format invalide. Veuillez saisir la date et l'heure au format AAAA/MM/JJ HH:MM:SS.")
                    address = input(f"Adresse de l'événement: ")
                    while True:
                        guests = input(f"Nombre d'invitées: ")
                        if guests == int:
                            break
                        else:
                            print("Veuillez indiquer un nombre entier.")
                    notes = input(f"Notes: ")
                    while True:
                        sales_contact_contract = input(f"Support référent (Nom et prénom): ")
                        if sales_contact_contract is None:
                            break
                        support = session.query(User).filter(User.name_lastname == sales_contact_contract).first()
                        if support and support.department == "SUP":
                            print(f"Souhaitez vous assigner {support.name_lastname} a l'événement?")
                            response = input("Oui ou Non?").strip().lower()
                            if response == "oui":
                                break
                            if response == "non":
                                print("Merci de renseigner le nom et le prénom d'un support à assigner à l'événement.")
                            else:
                                print("Erreur de frappe. Veuillez répondre par 'Oui' ou 'Non'.")
                        else:
                            print('Collaborateur inconnu de la base de données ou non attribué a la section "support". '
                                  "Merci de renseigner le nom et le prénom d'un collaborateur à assigner à l'événement.")

                    new_contract = cls(contract_id=contrat.id, customer_name_lastname=contrat.customer_name_lastname,
                                       customer_email=contrat.customer_email,
                                       customer_phone=contrat.customer_phone, title=title,
                                       date_hour_start=date_hour_start, date_hour_end=date_hour_end,
                                       address=address, guests=guests, notes=notes, sales_contact_contract= sales_contact_contract)

                    session.add(new_contract)
                    session.commit()
                    print("Votre événement a été créé avec succès!")
                    ManagementMenu.management_events_menu()

                if response == "non":
                    print("Création annulée. Vous allez être redirigée vers le Menu Événement.")
                    ManagementMenu.management_events_menu()

                else:
                    print("Erreur de frappe. Veuillez répondre par 'Oui' ou 'Non'.")

            else:
                print(f"Le contrat n°{contrat.id} n'a pas été signé par le client. Veuillez vous rapprocher de ce "
                      f"dernier.")

        if contrat is None:
            print("Erreur de frappe ou aucun contrat ne correspond a cette ID. Vous allez être redirigé vers le "
                  "Menu Événement.")
            ManagementMenu.management_events_menu()

    @classmethod
    def update_event(cls):
        print("Quel événement souhaitez-vous modifier?")
        id = input("ID de l'événement: ")

        event = session.query(Event).filter(Event.id == id).first()

        if event:
            print(f"\n-----MISE A JOUR DE L'ÉVÉNEMENT N°{id}-----")
            print(f"Souhaitez-vous conserver le contrat n°{event.contract_id} associé à cet événement?")
            response = input("Oui ou Non").strip().lower()
            if response == "oui":
                title = input(f"Nom de l'événement: {event.title}")
                while True:
                    date_hour_start = input(f"Date et heure du début de l'événement (format AAAA/MM/JJ HH:MM:SS)"
                                            f": {event.date_hour_start}")
                    if check_date_format(date_hour_start):
                        break
                    else:
                        print("Format invalide. Veuillez saisir la date et l'heure au format AAAA/MM/JJ HH:MM:SS.")
                while True:
                    date_hour_end = input(f"Date et heure de fin de l'événement (format AAAA/MM/JJ HH:MM:SS):"
                                          f" {event.date_hour_end}")
                    if check_date_format(date_hour_end):
                        break
                    else:
                        print(
                            "Format invalide. Veuillez saisir la date et l'heure au format AAAA/MM/JJ HH:MM:SS.")
                address = input(f"Adresse de l'événement: {event.adress}")
                while True:
                    guests = input(f"Nombre d'invitées: {event.guests}")
                    if guests == int:
                        break
                    else:
                        print("Veuillez indiquer un nombre entier.")
                notes = input(f"Notes: {event.notes}")
                while True:
                    sales_contact_contract = input(f"Support référent (Nom et prénom): {event.support_contact}")
                    if sales_contact_contract is None:
                        break
                    support = session.query(User).filter(User.name_lastname == sales_contact_contract).first()
                    if support and support.department == "SUP":
                        print(f"Souhaitez vous assigner {support.name_lastname} a l'événement?")
                        response = input("Oui ou Non?").strip().lower()
                        if response == "oui":
                            break
                        if response == "non":
                            print("Merci de renseigner le nom et le prénom d'un support à assigner à l'événement.")
                        else:
                            print("Erreur de frappe. Veuillez répondre par 'Oui' ou 'Non'.")
                    else:
                        print('Collaborateur inconnu de la base de données ou non attribué a la section "support". '
                              "Merci de renseigner le nom et le prénom d'un collaborateur à assigner à l'événement.")

                event.title = title
                event.date_hour_start = date_hour_start
                event.date_hour_end = date_hour_end
                event.adress = address
                event.guests = guests
                event.notes = notes
                event.support_contact = sales_contact_contract

                session.commit()
                print("L'événement a été correctement modifié!")
                ManagementMenu.management_events_menu()

            if response == "non":
                new_contract = input("ID du nouveau contrat à assigner à l'événement: ")
                contract = session.query(Contract).filter(Contract.id == new_contract).first()

                if contract:
                    if contract.contract_sign:
                        title = input(f"Nom de l'événement: {event.title}")
                        while True:
                            date_hour_start = input(f"Date et heure du début de l'événement (format AAAA/MM/JJ HH:MM:SS)"
                                                    f": {event.date_hour_start}")
                            if check_date_format(date_hour_start):
                                break
                            else:
                                print("Format invalide. Veuillez saisir la date et l'heure au format AAAA/MM/JJ HH:MM:SS.")
                        while True:
                            date_hour_end = input(f"Date et heure de fin de l'événement (format AAAA/MM/JJ HH:MM:SS):"
                                                  f" {event.date_hour_end}")
                            if check_date_format(date_hour_end):
                                break
                            else:
                                print(
                                    "Format invalide. Veuillez saisir la date et l'heure au format AAAA/MM/JJ HH:MM:SS.")
                        address = input(f"Adresse de l'événement: {event.adress}")
                        while True:
                            guests = input(f"Nombre d'invitées: {event.guests}")
                            if guests == int:
                                break
                            else:
                                print("Veuillez indiquer un nombre entier.")
                        notes = input(f"Notes: {event.notes}")
                        while True:
                            sales_contact_contract = input(f"Support référent (Nom et prénom): {event.support_contact}")
                            if sales_contact_contract is None:
                                break
                            support = session.query(User).filter(User.name_lastname == sales_contact_contract).first()
                            if support and support.department == "SUP":
                                print(f"Souhaitez vous assigner {support.name_lastname} a l'événement?")
                                response = input("Oui ou Non?").strip().lower()
                                if response == "oui":
                                    break
                                if response == "non":
                                    print(
                                        "Merci de renseigner le nom et le prénom d'un support à assigner à l'événement.")
                                else:
                                    print("Erreur de frappe. Veuillez répondre par 'Oui' ou 'Non'.")
                            else:
                                print(
                                    'Collaborateur inconnu de la base de données ou non attribué a la section "support". '
                                    "Merci de renseigner le nom et le prénom d'un collaborateur à assigner à l'événement.")

                        event.contract_id = contract.id
                        event.customer_name_lastname = contract.customer_name_lastname
                        event.customer_email = contract.customer_email
                        event.customer_phone = contract.customer_phone
                        event.title = title
                        event.date_hour_start = date_hour_start
                        event.date_hour_end = date_hour_end
                        event.adress = address
                        event.guests = guests
                        event.notes = notes
                        event.support_contact = sales_contact_contract

                        session.commit()
                        print("L'événement et le contrat associé ont été correctement modifié!")
                        ManagementMenu.management_events_menu()

                    else:
                        print(f"Le contrat n°{contract.id} n'a pas été signé par le client. Veuillez vous rapprocher de ce "
                            f"dernier. Vous allez être redirigé vers le Menu Événement.")
                        ManagementMenu.management_events_menu()

                else:
                    print("Erreur de frappe ou aucun contrat ne correspond a cette ID. Vous allez être redirigé vers le "
                        "Menu Événement.")
                    ManagementMenu.management_events_menu()

    @classmethod
    def update_event_support(cls, user):
        print("Quel événement souhaitez-vous modifier?")
        id = input("ID de l'événement: ")

        event = session.query(Event).filter(Event.id == id).first()

        if event.support_contact == user.name_lastname:
            if event:
                print(f"\n-----MISE A JOUR DE L'ÉVÉNEMENT N°{id}-----")
                title = input(f"Nom de l'événement: {event.title}")
                while True:
                    date_hour_start = input(f"Date et heure du début de l'événement (format AAAA/MM/JJ HH:MM:SS)"
                                            f": {event.date_hour_start}")
                    if check_date_format(date_hour_start):
                        break
                    else:
                        print("Format invalide. Veuillez saisir la date et l'heure au format AAAA/MM/JJ HH:MM:SS.")
                while True:
                    date_hour_end = input(f"Date et heure de fin de l'événement (format AAAA/MM/JJ HH:MM:SS):"
                                          f" {event.date_hour_end}")
                    if check_date_format(date_hour_end):
                        break
                    else:
                        print(
                            "Format invalide. Veuillez saisir la date et l'heure au format AAAA/MM/JJ HH:MM:SS.")
                address = input(f"Adresse de l'événement: {event.adress}")
                while True:
                    guests = input(f"Nombre d'invitées: {event.guests}")
                    if guests == int:
                        break
                    else:
                        print("Veuillez indiquer un nombre entier.")
                notes = input(f"Notes: {event.notes}")

                event.title = title
                event.date_hour_start = date_hour_start
                event.date_hour_end = date_hour_end
                event.adress = address
                event.guests = guests
                event.notes = notes

                session.commit()
                print("L'événement a été correctement modifié!")
                ManagementMenu.management_events_menu()

            else:
                print("Erreur de frappe ou aucun contrat ne correspond a cette ID. Vous allez être redirigé vers le "
                    "Menu Événement.")
                SupportMenu.support_events_menu()

        else:
            print("Vous n'êtes pas en change de cette événement. Vous allez être redirigé vers le Menu Événement.")
            SupportMenu.support_events_menu()
