from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text, Enum, Float, Boolean, BigInteger
from sqlalchemy.orm import relationship

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
