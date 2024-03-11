import hashlib
import re

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text, Enum, Float, Boolean, BigInteger
from sqlalchemy.orm import relationship
from database import session


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
    def find_user(cls, id):
        user = session.query(User).filter(User.id == id).first()
        return user

    @classmethod
    def create_user(cls, name_lastname, department, password, email):
        new_user = cls(name_lastname=name_lastname, department=department,
                       password=hashlib.sha256(password.encode()).hexdigest(), email=email)

        session.add(new_user)
        session.commit()

    @classmethod
    def delete_user(cls, user):
        session.delete(user)
        session.commit()

    @classmethod
    def update_user(cls, name_lastname, department, password, email, user):
        user.name_lastname = name_lastname
        user.departement = department
        if password.strip():
            user.password = hashlib.sha256(password.encode()).hexdigest()
        user.email = email

        session.commit()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_lastname = Column(String(45))
    email = Column(String(45))
    phone = Column(BigInteger)
    business_name = Column(String(45))
    date_first_contact = Column(DateTime, default=func.now())
    last_date_update = Column(DateTime, default=func.now())
    sales_contact = Column(Integer, ForeignKey('users.id'), unique=True)

    user = relationship('User', back_populates='customer')
    contract = relationship('Contract', back_populates='customer')

    @classmethod
    def find_customer(cls, id):
        customer = session.query(Customer).filter(Customer.id == id).first()
        return customer

    @classmethod
    def create_customer(cls, user, name_lastname, email, phone, business_name):
        new_customer = cls(name_lastname=name_lastname, email=email, phone=phone, business_name=business_name,
                           sales_contact=user.id)

        session.add(new_customer)
        session.commit()

    @classmethod
    def update_customer(cls, customer, name_lastname=None, email=None, phone=None, business_name=None):
        if name_lastname:
            customer.name_lastname = name_lastname
        if email:
            customer.email = email
        if phone:
            customer.phone = phone
        if business_name:
            customer.business_name = business_name

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
    def find_contract(cls, id):
        contract = session.query(Contract).filter(Contract.id == id).first()
        return contract

    @classmethod
    def create_contract(cls, total_amount, settled_amount, contract_sign, customer):
        new_contract = cls(customer_id=customer.id, total_amount=total_amount,
                           settled_amount=settled_amount, contract_sign=contract_sign)

        session.add(new_contract)
        session.commit()

    @classmethod
    def update_contract(cls, total_amount, settled_amount, contract_sign, contract):
        contract.total_amount = total_amount
        contract.settled_amount = settled_amount
        contract.contract_sign = contract_sign

        session.commit()

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
    def find_event(cls, id):
        event = session.query(Event).filter(Event.id == id).first()
        return event

    @classmethod
    def find_event_without_support(cls):
        events = session.query(Event).filter(Event.support_contact is None).all()
        return events

    @classmethod
    def create_event(cls, contract, title, date_hour_start, date_hour_end, address, guests, notes, sales_contact_contract):
        new_contract = cls(contract_id=contract.id, title=title,
                           date_hour_start=date_hour_start, date_hour_end=date_hour_end,
                           address=address, guests=guests, notes=notes, sales_contact_contract= sales_contact_contract)

        session.add(new_contract)
        session.commit()

    @classmethod
    def update_event(cls, event, title, date_hour_start, date_hour_end, address, guests, notes, sales_contact_contract):

        event.title = title
        event.date_hour_start = date_hour_start
        event.date_hour_end = date_hour_end
        event.adress = address
        event.guests = guests
        event.notes = notes
        event.support_contact = sales_contact_contract

        session.commit()

    @classmethod
    def update_event_for_support(cls, title, date_hour_start, date_hour_end, address, guests, notes, event):

        event.title = title
        event.date_hour_start = date_hour_start
        event.date_hour_end = date_hour_end
        event.adress = address
        event.guests = guests
        event.notes = notes

        session.commit()
