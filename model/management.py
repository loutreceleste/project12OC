from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text, Enum, Float, Boolean
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_lastname = Column(String(45))
    user_department = Column(Enum('COM', 'GES', 'SUP'))
    user_password = Column(String(45))
    user_email = Column(String(45))

    customer = relationship('Customer', back_populates='sales')
    contract = relationship('Contract', back_populates='sales')
    event = relationship('Event', back_populates='support')

class Contract(Base):
    __tablename__ = 'contracts'

    contract_id = Column(Integer, primary_key=True, autoincrement=True)
    contract_sales_id = Column(Integer, ForeignKey('users.id'))
    contract_customer_id = Column(Integer, ForeignKey('customers.id'))
    contract_total_amount = Column(Float)
    contract_settled_amount = Column(Float, default=0)
    contract_remaining_amount = Column(Float, default=0)
    contract_creation_date = Column(DateTime, default=func.now())
    contract_sign = Column(Boolean, default=False)

    sales = relationship('User', back_populates='contract')
    customer = relationship('Customer', back_populates='contract')
    event = relationship('Event', back_populates='contract')

class Event(Base):
    __tablename__ = 'events'

    event_id = Column(Integer, primary_key=True, autoincrement=True)
    event_contract_id = Column(Integer, ForeignKey('contracts.id'))
    event_customer_id = Column(Integer, ForeignKey('customers.id'))
    event_support_id = Column(Integer, ForeignKey('users.id'))
    event_title = Column(String(45))
    event_date_start = Column(DateTime)
    event_date_end = Column(DateTime)
    event_adress = Column(String(45))
    event_guests = Column(Float, default=0)
    event_notes = Column(Text)

    support = relationship('User', back_populates='event')
    contract = relationship('Contract', back_populates='event')
    customer = relationship('Customer', back_populates='event')