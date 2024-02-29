from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger, func
from sqlalchemy.orm import relationship

from database import session
from view.sales import SalesMenu, SalesCustomerViews

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

    @classmethod
    def create_customer(cls, user):
        name_lastname, email, phone, bussines_name = SalesCustomerViews.create_customer_view()

        new_customer = cls(name_lastname=name_lastname, email=email, phone=phone, bussines_name=bussines_name,
                           sales_contact=user.name_lastname)

        session.add(new_customer)
        session.commit()
        SalesCustomerViews.validation_customer_creation()
        SalesMenu.sale_customers_menu()


    @classmethod
    def update_customer(cls, user):
        id = SalesCustomerViews.update_customer_id_view()

        customer = session.query(Customer).filter(Customer.id == id).limit(1)

        if customer:
            if customer.sales_contact == user.name_lastname:
                name_lastname, email, phone, bussines_name = SalesCustomerViews.update_customer_view(customer)

                customer.name_lastname = name_lastname
                customer.email = email
                customer.phone = phone
                customer.bussines_name = bussines_name

                session.commit()
                SalesCustomerViews.validation_update_customer_view()
                SalesMenu.sale_customers_menu()

            else:
                SalesCustomerViews.not_in_charge_customer_view()
                SalesMenu.sale_customers_menu()

        else:
            SalesCustomerViews.none_customer_view()
            SalesMenu.sale_customers_menu()
