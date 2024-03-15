import hashlib
import re

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text, Enum, Float, Boolean, BigInteger, \
    and_, or_
from sqlalchemy.orm import relationship, aliased
from database import session


Base = declarative_base()

def check_date_format(date_str):
    pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"
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
    def find_user(cls):
        users = session.query(User).all()
        return users

    @classmethod
    def find_user_by_id(cls, id):
        user = session.query(User).filter(User.id == id).first()
        return user

    @classmethod
    def find_user_by_search(cls, search):
        users = session.query(User).filter(
            or_(
                User.id == search,
                User.name_lastname.startswith(f"%{search}%"),
                User.department.startswith(f"%{search}%"),
                User.email.startswith(f"%{search}%")
            )
        ).all()
        return users

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
        if name_lastname:
            user.name_lastname = name_lastname
        if department:
            user.departement = department
        if password.strip():
            user.password = hashlib.sha256(password.encode()).hexdigest()
        if email:
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
    def find_customer(cls):
        customers = session.query(Customer).all()
        return customers

    @classmethod
    def find_customer_by_user(cls, user):
        customers = session.query(Customer).filter(Customer.sales_contact == user.id).all()
        return customers

    @classmethod
    def find_customer_by_id(cls, id):
        customer = session.query(Customer).filter(Customer.id == id).first()
        return customer

    @classmethod
    def find_customer_by_search(cls, search):
        user_alias = aliased(User)
        customers = session.query(Customer).join(user_alias).filter(
            or_(
                Customer.id == search,
                Customer.name_lastname.startswith(f"%{search}%"),
                Customer.email.startswith(f"%{search}%"),
                Customer.business_name.startswith(f"%{search}%"),
                user_alias.name_lastname.startswith(f"%{search}%")
            )
        ).all()
        return customers

    @classmethod
    def create_customer(cls, user, name_lastname, email, phone, business_name):
        new_customer = cls(name_lastname=name_lastname, email=email, phone=phone, business_name=business_name,
                           sales_contact=user.id)

        session.add(new_customer)
        session.commit()

    @classmethod
    def update_customer(cls, customer, name_lastname, email, phone, business_name):
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
    def find_contract(cls):
        customer_alias = aliased(Customer)
        user_alias = aliased(User)

        contracts = session.query(Contract). \
            join(customer_alias, Contract.customer_id == customer_alias.id). \
            join(user_alias, customer_alias.sales_contact == user_alias.id).all()
        return contracts

    @classmethod
    def find_contract_by_search(cls, search):
        customer_alias = aliased(Customer)
        user_alias = aliased(User)

        contracts = session.query(Contract). \
            join(customer_alias, Contract.customer_id == customer_alias.id). \
            join(user_alias, customer_alias.sales_contact == user_alias.id).filter(
            or_(
                Contract.id == search,
                customer_alias.name_lastname.startswith(f"%{search}%"),
                Contract.total_amount == search,
                user_alias.name_lastname.startswith(f"%{search}%")
            )
        ).all()
        return contracts

    @classmethod
    def find_contract_by_id(cls, id):
        contract = session.query(Contract).filter(Contract.id == id).first()
        return contract

    @classmethod
    def find_contract_by_user(cls, user):
        contracts = (session.query(Contract).join(Contract.customer).join(Customer.user).filter(User.id == user.id)
                     .all())
        return contracts

    @classmethod
    def find_contract_not_sign(cls, user):
        contracts = session.query(Contract).join(Contract.customer).join(Customer.user).filter(
            and_(
                User.id == user.id,
                Contract.contract_sign == False
            )
        ).all()
        return contracts

    @classmethod
    def find_contract_remaining_amount(cls, user):
        contracts = session.query(Contract).join(Contract.customer).join(Customer.user).filter(
            and_(
                User.id == user.id,
                Contract.remaining_amount > 0
            )
        ).all()
        return contracts

    @classmethod
    def create_contract(cls, total_amount, settled_amount, contract_sign, customer):
        new_contract = cls(customer_id=customer.id, total_amount=total_amount,
                           settled_amount=settled_amount, contract_sign=contract_sign)

        session.add(new_contract)
        session.commit()

    @classmethod
    def update_contract(cls, contract, total_amount, settled_amount, contract_sign):
        if total_amount:
            contract.total_amount = total_amount
        if settled_amount:
            contract.settled_amount = settled_amount
        if contract_sign:
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
    def find_event(cls):
        contract_alias = aliased(Contract)
        customer_alias = aliased(Customer)
        user_alias = aliased(User)

        events = session.query(Event).join(contract_alias, Event.contract). \
            join(customer_alias, contract_alias.customer).outerjoin(user_alias, Event.user).all()
        return events

    @classmethod
    def find_event_by_search(cls, search):
        contract_alias = aliased(Contract)
        customer_alias = aliased(Customer)
        user_alias = aliased(User)

        events = (session.query(Event).join(contract_alias, Event.contract).
                  join(customer_alias, contract_alias.customer).outerjoin(user_alias, Event.user).filter(
            or_(
                Event.id == search,
                customer_alias.name_lastname.startswith(f"%{search}%"),
                Event.title.startswith(f"%{search}%"),
                user_alias.name_lastname.startswith(f"%{search}%")
            )
        ).all())
        return events

    @classmethod
    def find_event_by_id(cls, id):
        event = session.query(Event).filter(Event.id == id).first()
        return event

    @classmethod
    def find_event_without_support(cls):
        events = session.query(Event).filter(None == Event.support_contact).all()
        return events

    @classmethod
    def find_event_by_support(cls, user):
        events = session.query(Event).filter(Event.support_contact == user.name_lastname).all()
        return events

    @classmethod
    def create_event(cls, contract, title, date_hour_start, date_hour_end, address, guests, notes, support_contact):

            new_contract = cls(contract_id=contract.id, title=title,
                               date_hour_start=date_hour_start, date_hour_end=date_hour_end,
                               address=address, guests=guests, notes=notes, support_contact= support_contact)

            session.add(new_contract)
            session.commit()

    @classmethod
    def update_event(cls, event, title, date_hour_start, date_hour_end, address, guests, notes, support_id):
        if title:
            event.title = title
        if date_hour_start:
            event.date_hour_start = date_hour_start
        if date_hour_end:
            event.date_hour_end = date_hour_end
        if address:
            event.address = address
        if guests:
            event.guests = guests
        if notes:
            event.notes = notes
        if support_id:
            event.support_contact = support_id

        session.commit()

    @classmethod
    def update_event_for_support(cls, event, title, date_hour_start, date_hour_end, address, guests, notes):
        if title:
            event.title = title
        if date_hour_start:
            event.date_hour_start = date_hour_start
        if date_hour_end:
            event.date_hour_end = date_hour_end
        if address:
            event.adress = address
        if guests:
            event.guests = guests
        if notes:
            event.notes = notes

        session.commit()
