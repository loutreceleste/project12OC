from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger, func, Text
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_sales_id = Column(Integer, ForeignKey('users.id'))
    customer_lastname = Column(String(45))
    customer_email = Column(String(45))
    customer_phone = Column(BigInteger)
    customer_bussines_name = Column(String(45))
    customer_date_first_contact = Column(DateTime, default=func.now())
    customer_last_update = Column(DateTime, default=func.now())
    customer_event_contact = Column(Text)

    sales = relationship('User', back_populates='customer')
    event = relationship('Event', back_populates='customer')
