from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger, func, Text
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_lastname = Column(String(45))
    email = Column(String(45))
    phone = Column(BigInteger)
    bussines_name = Column(String(45))
    date_first_contact = Column(DateTime, default=func.now())
    last_date_update = Column(DateTime, default=func.now())
    sales_contact = Column(Integer, ForeignKey('users.name_lastname'))

    sales = relationship('User', back_populates='customer')
