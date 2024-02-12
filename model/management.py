from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger, func, Text, Enum
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

class Contract:
    def __init__(self, id, name, lastname, department, email):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.department = department
        self.email = email

class Event:
    def __init__(self, id, name, lastname, department, email):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.department = department
        self.email = email