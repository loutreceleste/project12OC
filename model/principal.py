import hashlib
import re

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text, Enum, Float, Boolean, BigInteger
from sqlalchemy.orm import relationship
from database import session

from view.management import ManagementMenu, ManagementUserViews, ManagementContractViews, ManagementEventViews
from view.support import SupportMenu
from view.sales import SalesMenu, SalesCustomerViews


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

    customer = relationship('Customer', back_populates='user')
    event = relationship('Event', back_populates='user')

    @classmethod
    def create_user(cls, name_lastname, department, password, email):

        new_user = cls(name_lastname=name_lastname, department=department,
                       password=hashlib.sha256(password.encode()).hexdigest(), email=email)

        session.add(new_user)
        session.commit()


    @classmethod
    def delete_user(cls):
        from view.principal import MainView
        id = ManagementUserViews.delete_user_id_view()

        user = session.query(User).filter(User.id == id).limit(1)
        if user:
            while True:
                ManagementUserViews.confirmation_delete_user_view(user)
                response = MainView.oui_non_input()

                if response == "oui":
                    session.delete(user)
                    session.commit()
                    ManagementUserViews.validation_delete_user_view(user)
                    break

                elif response == "non":
                    ManagementUserViews.cancelation_delete_user_view()
                    break

                else:
                    MainView.error_oui_non_input()

            ManagementMenu.management_users_menu()

        else:
            ManagementUserViews.none_user_view()
            ManagementMenu.management_users_menu()

    @classmethod
    def update_user(cls):
        id = ManagementUserViews.update_user_id_view()

        user = session.query(User).filter(User.id == id).limit(1)
        if user:
            name_lastname, department, password, email = ManagementUserViews.update_user_view(user, id)

            user.name_lastname = name_lastname
            user.departement = department
            if password.strip():
                user.password = hashlib.sha256(password.encode()).hexdigest()
            user.email = email

            session.commit()
            ManagementUserViews.validation_update_user_view(user)
            ManagementMenu.management_users_menu()

        else:
            ManagementUserViews.none_user_view()
            ManagementMenu.management_users_menu()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_lastname = Column(String(45))
    email = Column(String(45))
    phone = Column(BigInteger)
    bussines_name = Column(String(45))
    date_first_contact = Column(DateTime, default=func.now())
    last_date_update = Column(DateTime, default=func.now())
    sales_id = Column(Integer, ForeignKey('users.id'), unique=True)

    user = relationship('User', back_populates='customer')
    contract = relationship('Contract', back_populates='customer')

    @classmethod
    def create_customer(cls, user, name_lastname, email, phone, bussines_name):

        new_customer = cls(name_lastname=name_lastname, email=email, phone=phone, bussines_name=bussines_name,
                           sales_contact=user.name_lastname)

        session.add(new_customer)
        session.commit()

    @classmethod
    def find_customer(cls, id):
        customer = session.query(Customer).filter(Customer.id == id).limit(1)
        return customer

    @classmethod
    def update_customer(cls, customer, name_lastname, email, phone, bussines_name):

        customer.name_lastname = name_lastname
        customer.email = email
        customer.phone = phone
        customer.bussines_name = bussines_name

        session.commit()



class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), unique=True)
    total_amount = Column(Float, default=0)
    settled_amount = Column(Float, default=0)
    remaining_amount = Column(Float, default=0)
    creation_date = Column(DateTime, default=func.now())
    contract_sign = Column(Boolean, default=False)

    customer = relationship('Customer', back_populates='contract')
    event = relationship('Event', back_populates='contract')

    @classmethod
    def create_contract(cls):
        from view.principal import MainView
        id = ManagementContractViews.create_contract_id_customer_view()

        customer = session.query(Customer).filter(Customer.id == id).limit(1)

        if customer:
            ManagementContractViews.confirmation_create_contract_view(customer)
            response = MainView.oui_non_input()

            while True:
                if response == "oui":
                    total_amount, settled_amount, contract_sign = ManagementContractViews.create_contract_view()

                    new_contract = cls(customer_name_lastname=customer.name_lastname, customer_email=customer.email,
                                       customer_phone=customer.phone, total_amount=total_amount,
                                       settled_amount=settled_amount, contract_sign=contract_sign,
                                       sales_contact_contract=customer.sales_contact)

                    session.add(new_contract)
                    session.commit()
                    ManagementContractViews.validation_create_contract_view()
                    break

                if response == "non":
                    ManagementContractViews.cancelation_create_contract_view()
                    break

                else:
                    MainView.error_oui_non_input()

            ManagementMenu.management_contrats_menu()

        else:
            ManagementContractViews.none_customer_view()
            ManagementMenu.management_contrats_menu()

    @classmethod
    def update_contract(cls):
        id = ManagementContractViews.update_contract_id_view()

        contract = session.query(Contract).filter(Contract.id == id).limit(1)

        if contract:
            total_amount, settled_amount, contract_sign = ManagementContractViews.update_contract_view(contract, id)

            contract.total_amount = total_amount
            contract.settled_amount = settled_amount
            contract.contract_sign = contract_sign

            session.commit()
            ManagementContractViews.validation_update_contract_view()
            ManagementMenu.management_contrats_menu()

        else:
            ManagementContractViews.none_contract_view()
            ManagementMenu.management_contrats_menu()

    @classmethod
    def update_contract_for_sales(cls, user):
        id = ManagementContractViews.update_contract_id_view()

        contract = session.query(Contract).filter(Contract.id == id).limit(1)

        if contract.sales_contact_contract == user.name_lastname:
            if contract:
                total_amount, settled_amount, contract_sign = ManagementContractViews.update_contract_view(contract, id)

                contract.total_amount = total_amount
                contract.settled_amount = settled_amount
                contract.contract_sign = contract_sign

                session.commit()
                ManagementContractViews.validation_update_contract_view()
                SalesMenu.sale_contracts_menu()

            else:
                ManagementContractViews.none_contract_view()
                SalesMenu.sale_contracts_menu()

        else:
            ManagementContractViews.not_in_charge_contract_view()
            SalesMenu.sale_contracts_menu()


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    contract_id = Column(Integer, ForeignKey('contracts.id'), unique=True)
    title = Column(String(45))
    date_hour_start = Column(DateTime)
    date_hour_end = Column(DateTime)
    address = Column(String(45))
    guests = Column(Integer, default=0)
    notes = Column(Text)
    support_contact = Column(Integer, ForeignKey('users.id'))

    contract = relationship('Contract', back_populates='event')
    user = relationship('User', back_populates='event')

    @classmethod
    def create_event(cls):
        from view.principal import MainView
        id = ManagementEventViews.create_event_id_contract_view()

        contrat = session.query(Contract).filter(Contract.id == id).limit(1)

        if contrat:
            if contrat.contract_sign:
                ManagementEventViews.confirmation_create_event_view(contrat)
                response = MainView.oui_non_input()

                while True:
                    if response == "oui":
                        title, date_hour_start, date_hour_end, address, guests, notes, sales_contact_contract = (
                            ManagementEventViews.create_event_view())

                        new_contract = cls(contract_id=contrat.id, customer_name_lastname=contrat.customer_name_lastname,
                                           customer_email=contrat.customer_email,
                                           customer_phone=contrat.customer_phone, title=title,
                                           date_hour_start=date_hour_start, date_hour_end=date_hour_end,
                                           address=address, guests=guests, notes=notes, sales_contact_contract= sales_contact_contract)

                        session.add(new_contract)
                        session.commit()
                        ManagementEventViews.validation_create_event_view()
                        break

                    if response == "non":
                        ManagementEventViews.cancelation_create_event_view()
                        break

                    else:
                        MainView.error_oui_non_input()

                SalesMenu.sale_events_menu()

            else:
                ManagementEventViews.not_sign_contract_view(contrat)
                SalesMenu.sale_events_menu()

        else:
            ManagementEventViews.none_event_view()
            SalesMenu.sale_events_menu()

    @classmethod
    def update_event(cls):
        id = ManagementEventViews.update_event_id_contract_view()

        event = session.query(Event).filter(Event.id == id).limit(1)

        if event:
            title, date_hour_start, date_hour_end, address, guests, notes, sales_contact_contract = (
                ManagementEventViews.update_event_view(event, id))

            event.title = title
            event.date_hour_start = date_hour_start
            event.date_hour_end = date_hour_end
            event.adress = address
            event.guests = guests
            event.notes = notes
            event.support_contact = sales_contact_contract

            session.commit()
            ManagementEventViews.validation_update_event_view()
            ManagementMenu.management_events_menu()

        else:
            ManagementEventViews.none_event_view()
            ManagementMenu.management_events_menu()

    @classmethod
    def update_event_for_support(cls, user):
        id = ManagementEventViews.update_event_id_contract_view()

        event = session.query(Event).filter(Event.id == id).limit(1)

        if event.support_contact == user.name_lastname:
            if event:
                title, date_hour_start, date_hour_end, address, guests, notes, sales_contact_contract = (
                    ManagementEventViews.update_event_view(event, id))

                event.title = title
                event.date_hour_start = date_hour_start
                event.date_hour_end = date_hour_end
                event.adress = address
                event.guests = guests
                event.notes = notes

                session.commit()
                ManagementEventViews.validation_update_event_view()
                SupportMenu.support_events_menu()

            else:
                ManagementEventViews.none_event_view()
                SupportMenu.support_events_menu()

        else:
            ManagementEventViews.not_in_charge_event_view()
            SupportMenu.support_events_menu()
