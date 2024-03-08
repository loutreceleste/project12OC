from view.management import ManagementContractViews, ManagementEventViews
from view.sales import SalesMenu, SalesCustomerViews, SalesSearchViews
from view.principal import MainView, MainSearch
from model.principal import Customer, Contract, Event


class SalesController(SalesMenu):
    def __init__(self, user):
        SalesMenu.sale_menu()
        choice = MainView.choise()
        handle_sales_choise(choice, user)

def handle_sales_choise(choice, user):

    if choice == '1':
        SalesMenu.sale_customers_menu()
        choice = MainView.choise()
        while choice:
            if choice == '1':
                name_lastname, email, phone, bussines_name = SalesCustomerViews.create_customer_view()
                Customer.create_customer(user, name_lastname, email, phone, bussines_name)
                SalesCustomerViews.validation_customer_creation()
            if choice == '2':
                id = SalesCustomerViews.update_customer_id_view()
                customer = Customer.find_customer(id)
                if customer:
                    if customer.sales_contact == user.id:
                        name_lastname, email, phone, business_name = SalesCustomerViews.update_customer_view(customer)
                        Customer.update_customer(customer, name_lastname, email, phone, business_name)
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
        while choice:
            if choice == '1':
                id = ManagementContractViews.update_contract_id_view()
                contract = Contract.find_contract(id)
                if contract:
                    total_amount, settled_amount, contract_sign = Contract.update_contract_view(contract, id)
                    Contract.update_contract(total_amount, settled_amount, contract_sign, contract)
                    ManagementContractViews.validation_update_contract_view()
                else:
                    ManagementContractViews.none_contract_view()
            if choice == '2':
                MainSearch.show_all_contracts()
            if choice == '3':
                SalesSearchViews.show_my_contracts(user)
            if choice == '4':
                SalesSearchViews.show_my_contracts_not_sign(user)
            if choice == '5':
                SalesSearchViews.show_my_contracts_remaining_amount(user)
            if choice == '6':
                MainSearch.show_all_contracts_search()
            if choice == '7':
                SalesController(user)

            SalesMenu.sale_contracts_menu()
            choice = MainView.choise()

    if choice == '3':
        SalesMenu.sale_events_menu()
        choice = MainView.choise()
        while choice:
            if choice == '1':
                id = ManagementEventViews.create_event_id_contract_view()
                contract = Event.find_contract(id)
                if contract:
                    if contract.contract_sign:
                        ManagementEventViews.confirmation_create_event_view(contract)
                        response = MainView.oui_non_input()
                        while True:
                            if response == "oui":
                                title, date_hour_start, date_hour_end, address, guests, notes, sales_contact_contract \
                                    = ManagementEventViews.create_event_view()
                                Event.create_event(contract, title, date_hour_start, date_hour_end, address, guests,
                                             notes, sales_contact_contract)
                                ManagementEventViews.validation_create_event_view()
                                break

                            if response == "non":
                                ManagementEventViews.cancelation_create_event_view()
                                break

                            else:
                                MainView.error_oui_non_input()
                    else:
                        ManagementEventViews.not_sign_contract_view(contract)
                else:
                    ManagementEventViews.none_event_view()
            if choice == '2':
                MainSearch.show_all_events()
            if choice == '3':
                MainSearch.show_all_events_search()
            if choice == '4':
                SalesController(user)

            SalesMenu.sale_events_menu()
            choice = MainView.choise()
    if choice == '4':
        exit()