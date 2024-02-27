from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger, func, Text
from sqlalchemy.orm import relationship

from database import session
from view.sales import SalesMenu

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
        print("\n-----NOUVEAU CLIENT-----")
        name_lastname = input("Nom et prénom du client: ")
        email = input("Email du client: ")
        while True:
            phone = input("Téléphone du client: ")
            if phone.isdigit():
                phone = int(phone)
            else:
                print("Veuillez indiquer un numéro de téléphone.")
        bussines_name = input("Nom commercial du client: ")

        new_customer = cls(name_lastname=name_lastname, email=email, phone=phone, bussines_name=bussines_name,
                           sales_contact=user.name_lastname)

        session.add(new_customer)
        session.commit()
        print("Votre client a été correctement crée. Vous allez être redirigée vers le Menu Commercial")
        SalesMenu.sale_customers_menu()


    @classmethod
    def update_customer(cls, user):
        print("Quel client souhaitez vous modifier?")
        id = input("ID du cleint a modifier: ")

        customer = session.query(Customer).filter(Customer.id == id).first()

        if customer:
            if customer.sales_contact == user.name_lastname:
                print(f"\n-----MISE A JOUR DU CLIENT N°{customer.id}-----")
                name_lastname = input(f"Nom et prénom du client: {customer.name_lastname}")
                email = input(f"Email du client: {customer.email}")
                while True:
                    phone = input(f"Téléphone du client: {customer.phone}")
                    if phone == int:
                        break
                    else:
                        print("Veuillez indiquer un numéro de téléphone.")
                bussines_name = input(f"Nom commercial du client: {customer.bussines_name}")

                customer.name_lastname = name_lastname
                customer.email = email
                customer.phone = phone
                customer.bussines_name = bussines_name

                session.commit()
                print("La fiche de votre client a bien été modifié!")
                SalesMenu.sale_customers_menu()

            else:
                print("Vous n'êtes pas en change de ce client. Vous allez être redirigé vers le Menu Commercial.")
                SalesMenu.sale_customers_menu()

        else:
            print("Erreur de frappe ou aucun client ne correspond a cette ID. Vous allez être redirigé vers le "
                  "Menu Commercial.")
            SalesMenu.sale_customers_menu()
