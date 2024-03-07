from view.management import ManagementUserViews
from view.sales import SalesMenu, SalesCustomerViews, SalesSearchViews
from view.principal import MainView, MainSearch
from model.principal import Customer

class SalesController(SalesMenu):
    def __init__(self, user):
        SalesMenu.sale_menu()
        choice = MainView.choise()
        handle_sales_choise(choice, user)

def handle_sales_choise(choice, user):
    if choice == '1':
        SalesMenu.sale_customers_menu()
        choice = MainView.choise()
        while choice != '6':
            if choice == '1':
                name_lastname, email, phone, bussines_name = SalesCustomerViews.create_customer_view()
                Customer.create_customer(user, name_lastname, email, phone, bussines_name)
                SalesCustomerViews.validation_customer_creation()
            if choice == '2':
                name_lastname, email, phone, bussines_name, id = SalesCustomerViews.update_customer_id_view()
                customer = Customer.find_customer(id)
                if customer:
                    if customer.sales_contact == user.name_lastname:
                        Customer.update_customer(customer, name_lastname, email, phone, bussines_name)
                        SalesCustomerViews.validation_update_customer_view()
                    else:
                        SalesCustomerViews.not_in_charge_customer_view()
                else:
                    SalesCustomerViews.none_customer_view()
            if choice == '3':
                MainSearch.show_all_customers()
            if choice == '4':
                MainSearch.show_all_customers_search()
            if choice == '5':
                SalesSearchViews.show_my_customers(user)
            if choice == '6':
                SalesController(user)

            SalesMenu.sale_customers_menu()
            choice = MainView.choise()

    if choice == '2':
        SalesMenu.sale_contracts_menu()
        choice = MainView.choise()
    if choice == '3':
        SalesMenu.sale_events_menu()
        choice = MainView.choise()
    if choice == '4':
        exit()