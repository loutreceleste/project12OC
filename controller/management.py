from model.principal import User, Customer, Contract, Event
from view.management import ManagementMenu, ManagementUserViews, ManagementContractViews, ManagementEventViews, \
    ManagmentSearchViews
from view.principal import MainView, MainSearch


class ManagementController(ManagementMenu):
    def __init__(self, user):
        ManagementMenu.management_menu()
        choice = MainView.choise()
        handle_management_choise(choice, user)

def handle_management_choise(choice, user):

    while True:
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 5:
                if choice == 1:
                    ManagementMenu.management_users_menu()
                    choice = MainView.choise()

                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 6:
                                if choice == 1:
                                    name_lastname, department, password, email = ManagementUserViews.create_user_view()
                                    User.create_user(name_lastname, department, password, email)
                                    ManagementUserViews.validation_user_creation(name_lastname)
                                if choice == 2:
                                    id = ManagementUserViews.update_user_id_view()
                                    user = User.find_user_by_id(id)
                                    if user:
                                        name_lastname, department, password, email = (
                                            ManagementUserViews.update_user_view(user, id))
                                        User.update_user(name_lastname, department, password, email, user)
                                        ManagementUserViews.validation_update_user_view(user)
                                    else:
                                        ManagementUserViews.none_user_view()
                                if choice == 3:
                                    id = ManagementUserViews.delete_user_id_view()
                                    user = User.find_user_by_id(id)
                                    if user:
                                        while True:
                                            ManagementUserViews.confirmation_delete_user_view(user)
                                            response = MainView.oui_non_input()
                                            if response == "oui":
                                                User.delete_user(user)
                                                ManagementUserViews.validation_delete_user_view(user)
                                                break
                                            elif response == "non":
                                                ManagementUserViews.cancelation_delete_user_view()
                                                break
                                            else:
                                                MainView.error_oui_non_input()
                                    else:
                                        ManagementUserViews.none_user_view()
                                if choice == 4:
                                    search = MainSearch.search_all_users_search()
                                    users = User.find_user_by_search(search)
                                    if users:
                                        MainSearch.show_all_users_search(users)
                                    else:
                                        MainView.message_no_user_whith_search()
                                if choice == 5:
                                    users = User.find_user()
                                    if users:
                                        MainSearch.show_all_users(users)
                                    else:
                                        MainView.message_no_user()
                                if choice == 6:
                                    ManagementController(user)
                            else:
                                print("Veuillez saisir un nombre entre 1 et 6!")
                        else:
                            MainView.message_no_whole_number()

                        ManagementMenu.management_users_menu()
                        choice = MainView.choise()
                if choice == 2:
                    ManagementMenu.management_customers_menu()
                    choice = MainView.choise()

                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 3:
                                if choice == 1:
                                    customers = Customer.find_customer()
                                    if customers:
                                        MainSearch.show_all_customers(customers)
                                    else:
                                        MainView.message_no_customer()
                                elif choice == 2:
                                    search = MainSearch.search_all_customers_search()
                                    customers = Customer.find_customer_by_search(search)
                                    if customers:
                                        MainSearch.show_all_customers_search(customers)
                                    else:
                                        MainView.message_no_customer_whith_search()
                                elif choice == 3:
                                    ManagementController(user)
                            else:
                                print("Veuillez saisir un nombre entre 1 et 3!")
                        else:
                            MainView.message_no_whole_number()

                        ManagementMenu.management_customers_menu()
                        choice = MainView.choise()
                if choice == 3:
                    ManagementMenu.management_contrats_menu()
                    choice = MainView.choise()

                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 5:
                                if choice == 1:
                                    id = ManagementContractViews.create_contract_id_customer_view()
                                    customer = Customer.find_customer_by_id(id)
                                    if customer:
                                        ManagementContractViews.confirmation_create_contract_view(customer)
                                        response = MainView.oui_non_input()

                                        while True:
                                            if response == "oui":
                                                total_amount, settled_amount, contract_sign = (
                                                    ManagementContractViews.create_contract_view())
                                                Contract.create_contract(total_amount, settled_amount, contract_sign,
                                                                         customer)
                                                ManagementContractViews.validation_create_contract_view()
                                                break

                                            if response == "non":
                                                ManagementContractViews.cancelation_create_contract_view()
                                                break
                                            else:
                                                MainView.error_oui_non_input()
                                    else:
                                        ManagementContractViews.none_customer_view()
                                elif choice == 2:
                                    id = ManagementContractViews.update_contract_id_view()
                                    contract = Contract.find_contract_by_id(id)
                                    if contract:
                                        total_amount, settled_amount, contract_sign = (
                                            ManagementContractViews.update_contract_view(
                                            contract, id))
                                        Contract.update_contract(contract, total_amount, settled_amount, contract_sign)
                                        ManagementContractViews.validation_update_contract_view()
                                    else:
                                        ManagementContractViews.none_contract_view()
                                elif choice == 3:
                                    contracts = Contract.find_contract()
                                    if contracts:
                                        MainSearch.show_all_contracts(contracts)
                                    else:
                                        MainView.message_no_contract()
                                elif choice == 4:
                                    search = MainSearch.search_all_contracts_search()
                                    contracts = Contract.find_contract_by_search(search)
                                    if contracts:
                                        MainSearch.show_all_contracts_search(contracts)
                                    else:
                                        MainView.message_no_contract_whith_search()
                                elif choice == 5:
                                    ManagementController(user)
                            else:
                                print("Veuillez saisir un nombre entre 1 et 5!")
                        else:
                            MainView.message_no_whole_number()

                        ManagementMenu.management_contrats_menu()
                        choice = MainView.choise()
                if choice == 4:
                    ManagementMenu.management_events_menu()
                    choice = MainView.choise()
                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 5:
                                if choice == 1:
                                    id = ManagementEventViews.update_event_id_contract_view()
                                    event = Event.find_event_by_id(id)
                                    if event:
                                        (title, date_hour_start, date_hour_end, address, guests, notes,
                                         support_id) = (ManagementEventViews.update_event_view(event, id))
                                        Event.update_event(event, title, date_hour_start, date_hour_end, address,
                                                           guests, notes, support_id)
                                        ManagementEventViews.validation_update_event_view()
                                    else:
                                        ManagementEventViews.none_event_view()
                                elif choice == 2:
                                    events = Event.find_event()
                                    if events:
                                        MainSearch.show_all_events(events)
                                    else:
                                        MainView.message_no_event()
                                elif choice == 3:
                                    search = MainSearch.search_all_events_search()
                                    events = MainSearch.show_all_events_search(search)
                                    if events:
                                        MainSearch.show_all_events_search(events)
                                    else:
                                        MainView.message_no_event_whith_search()
                                elif choice == 4:
                                    events = Event.find_event_without_support()
                                    if events:
                                        ManagmentSearchViews.show_all_events_no_support(events)
                                    else:
                                        ManagementEventViews.all_event_assigned()
                                elif choice == 5:
                                    ManagementController(user)
                            else:
                                print("Veuillez saisir un nombre entre 1 et 5!")
                        else:
                            MainView.message_no_whole_number()

                        ManagementMenu.management_events_menu()
                        choice = MainView.choise()

                if choice == 5:
                    exit()

            else:
                print("Veuillez saisir un nombre entre 1 et 5!")
        else:
            MainView.message_no_whole_number()

        ManagementController(user)
        choice = MainView.choise()
