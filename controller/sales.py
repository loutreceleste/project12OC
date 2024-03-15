import sqlalchemy

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

    while True:
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                if choice == 1:
                    SalesMenu.sale_customers_menu()
                    choice = MainView.choise()

                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 6:
                                if choice == 1:
                                    name_lastname, email, phone, business_name = (
                                        SalesCustomerViews.create_customer_view())
                                    Customer.create_customer(user, name_lastname, email, phone, business_name)
                                    SalesCustomerViews.validation_customer_creation()
                                if choice == 2:
                                    id = SalesCustomerViews.update_customer_id_view()
                                    customer = Customer.find_customer_by_id(id)
                                    if customer:
                                        if customer.sales_contact == user.id:
                                            name_lastname, email, phone, business_name = (
                                                SalesCustomerViews.update_customer_view(customer))
                                            Customer.update_customer(customer, name_lastname, email, phone,
                                                                     business_name)
                                            SalesCustomerViews.validation_update_customer_view()
                                        else:
                                            SalesCustomerViews.not_in_charge_customer_view()
                                    else:
                                        SalesCustomerViews.none_customer_view()
                                if choice == 3:
                                    MainSearch.show_all_customers()
                                if choice == 4:
                                    MainSearch.show_all_customers_search()
                                if choice == 5:
                                    customers = Customer.find_customer_by_user(user)
                                    if customers:
                                        SalesSearchViews.show_my_customers(customers)
                                    else:
                                        print("Aucun client trouvé avec cette recherche.")
                                if choice == 6:
                                    SalesController(user)
                            else:
                                print("Veuillez saisir un nombre entre 1 et 6!")
                        else:
                            MainView.message_no_whole_number()

                        SalesMenu.sale_customers_menu()
                        choice = MainView.choise()

                elif choice == 2:
                    SalesMenu.sale_contracts_menu()
                    choice = MainView.choise()

                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 7:
                                if choice == 1:
                                    id = ManagementContractViews.update_contract_id_view()
                                    contract = Contract.find_contract_by_id(id)
                                    if contract:
                                        if user.id == contract.customer.id:
                                            total_amount, settled_amount, contract_sign = (
                                                ManagementContractViews.update_contract_view(contract, id))
                                            Contract.update_contract(contract, total_amount, settled_amount,
                                                                     contract_sign)
                                            ManagementContractViews.validation_update_contract_view()
                                        else:
                                            SalesCustomerViews.not_in_charge_customer_view()
                                    else:
                                        ManagementContractViews.none_contract_view()
                                if choice == 2:
                                    MainSearch.show_all_contracts()
                                if choice == 3:
                                    contracts = Contract.find_contract_by_user(user)
                                    if contracts:
                                        SalesSearchViews.show_my_contracts(contracts)
                                    else:
                                        SalesCustomerViews.no_contract_view()
                                if choice == 4:
                                    contracts = Contract.find_contract_not_sign(user)
                                    if contracts:
                                        SalesSearchViews.show_my_contracts_not_sign(contracts)
                                    else:
                                        SalesCustomerViews.all_contract_sign_view()
                                if choice == 5:
                                    contracts = Contract.find_contract_remaining_amount(user)
                                    if contracts:
                                        SalesSearchViews.show_my_contracts_remaining_amount(contracts)
                                    else:
                                        SalesCustomerViews.all_contract_settled()
                                if choice == 6:
                                    MainSearch.show_all_contracts_search()
                                if choice == 7:
                                    SalesController(user)
                            else:
                                print("Veuillez saisir un nombre entre 1 et 7!")
                        else:
                            MainView.message_no_whole_number()

                        SalesMenu.sale_contracts_menu()
                        choice = MainView.choise()

                elif choice == 3:
                    SalesMenu.sale_events_menu()
                    choice = MainView.choise()

                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 4:
                                if choice == 1:
                                    id = ManagementEventViews.create_event_id_contract_view()
                                    contract = Contract.find_contract_by_id(id)
                                    if user.id == contract.customer.sales_contact:
                                        if contract:
                                            if contract.contract_sign:
                                                ManagementEventViews.confirmation_create_event_view(contract)
                                                response = MainView.oui_non_input()
                                                while True:
                                                    if response == "oui":
                                                        (title, date_hour_start, date_hour_end, address, guests, notes,
                                                         support_contact) = ManagementEventViews.create_event_view()
                                                        try:
                                                            Event.create_event(contract, title, date_hour_start,
                                                                               date_hour_end, address, guests, notes,
                                                                               support_contact)
                                                            ManagementEventViews.validation_create_event_view()
                                                        except sqlalchemy.exc.OperationalError:
                                                            SalesCustomerViews.wrong_date_format()
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
                                    else:
                                        SalesCustomerViews.not_in_charge_customer_view()
                                if choice == 2:
                                    MainSearch.show_all_events()
                                if choice == 3:
                                    MainSearch.show_all_events_search()
                                if choice == 4:
                                    SalesController(user)
                            else:
                                print("Veuillez saisir un nombre entre 1 et 4!")
                        else:
                            MainView.message_no_whole_number()

                        SalesMenu.sale_events_menu()
                        choice = MainView.choise()

                elif choice == 4:
                    exit()
            else:
                print("Veuillez saisir un nombre entre 1 et 4!")
        else:
            MainView.message_no_whole_number()

        SalesController(user)
        choice = MainView.choise()
