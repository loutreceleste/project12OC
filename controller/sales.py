import sqlalchemy

from view.management import ManagementContractViews, ManagementEventViews
from view.sales import SalesMenu, SalesCustomerViews, SalesSearchViews
from view.principal import MainView, MainSearch
from model.principal import Customer, Contract, Event


class SalesController(SalesMenu):
    def __init__(self, user):
        # Display the sales menu
        SalesMenu.sale_menu()
        # Get user's choice
        choice = MainView.choise()
        # Handle user's sales choice
        handle_sales_choice(choice, user)


def handle_sales_choice(choice, user):
    while True:
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                if choice == 1:
                    # Sales management for customers
                    SalesMenu.sale_customers_menu()
                    choice = MainView.choise()

                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 6:
                                if choice == 1:
                                    # Create a new customer
                                    (name_lastname, email, phone,
                                     business_name) = (SalesCustomerViews
                                                       .create_customer_view())
                                    Customer.create_customer(user,
                                                             name_lastname,
                                                             email, phone,
                                                             business_name)
                                    (SalesCustomerViews.
                                     validation_customer_creation())
                                if choice == 2:
                                    # Update an existing customer
                                    id = (SalesCustomerViews.
                                          update_customer_id_view())
                                    customer = Customer.find_customer_by_id(id)
                                    if customer:
                                        if customer.sales_contact == user.id:
                                            (name_lastname, email, phone,
                                             business_name) = (
                                                SalesCustomerViews.
                                                update_customer_view(customer))
                                            (Customer.
                                             update_customer(customer,
                                                             name_lastname,
                                                             email, phone,
                                                             business_name))
                                            (SalesCustomerViews.
                                             validation_update_customer_view())
                                        else:
                                            (SalesCustomerViews.
                                             not_in_charge_customer_view())
                                    else:
                                        SalesCustomerViews.none_customer_view()
                                if choice == 3:
                                    # Show all customers
                                    customers = Customer.find_customer()
                                    if customers:
                                        (MainSearch.
                                         show_all_customers(customers))
                                    else:
                                        MainView.message_no_customer()
                                if choice == 4:
                                    # Search for customers
                                    search = (MainSearch.
                                              search_all_customers_search())
                                    customers = (Customer.
                                                 find_customer_by_search
                                                 (search))
                                    if customers:
                                        (MainSearch.
                                         show_all_customers_search(customers))
                                    else:
                                        (MainView.
                                         message_no_customer_whith_search())
                                if choice == 5:
                                    # Show customers managed by the current
                                    # user
                                    customers = (Customer.find_customer_by_user
                                                 (user))
                                    if customers:
                                        (SalesSearchViews.show_my_customers
                                         (customers))
                                    else:
                                        print("No client found with this "
                                              "search.")
                                if choice == 6:
                                    # Go back to the main menu
                                    SalesController(user)
                            else:
                                print("Please enter a number between 1 and 6!")
                        else:
                            MainView.message_no_whole_number()

                        SalesMenu.sale_customers_menu()
                        choice = MainView.choise()

                elif choice == 2:
                    # Sales management for contracts
                    SalesMenu.sale_contracts_menu()
                    choice = MainView.choise()

                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 7:
                                if choice == 1:
                                    # Update an existing contract
                                    id = (ManagementContractViews.
                                          update_contract_id_view())
                                    contract = Contract.find_contract_by_id(id)
                                    if contract:
                                        if (user.id
                                                == contract.customer.user.id):
                                            (total_amount, settled_amount,
                                             contract_sign) = (
                                                ManagementContractViews.
                                                update_contract_view(contract,
                                                                     id))
                                            (Contract.
                                             update_contract(contract,
                                                             total_amount,
                                                             settled_amount,
                                                             contract_sign))
                                            (ManagementContractViews.
                                             validation_update_contract_view())
                                        else:
                                            (SalesCustomerViews.
                                             not_in_charge_customer_view())
                                    else:
                                        (ManagementContractViews.
                                         none_contract_view())
                                if choice == 2:
                                    # Show all contracts
                                    contracts = Contract.find_contract()
                                    if contracts:
                                        (MainSearch.show_all_contracts
                                         (contracts))
                                    else:
                                        MainView.message_no_contract()
                                if choice == 3:
                                    # Show contracts managed by the current
                                    # user
                                    contracts = (Contract.find_contract_by_user
                                                 (user))
                                    if contracts:
                                        (SalesSearchViews.show_my_contracts
                                         (contracts))
                                    else:
                                        SalesCustomerViews.no_contract_view()
                                if choice == 4:
                                    # Show unsigned contracts
                                    contracts = (Contract.
                                                 find_contract_not_sign(user))
                                    if contracts:
                                        (SalesSearchViews.
                                         show_my_contracts_not_sign(contracts))
                                    else:
                                        (SalesCustomerViews.
                                         all_contract_sign_view())
                                if choice == 5:
                                    # Show contracts with remaining amount
                                    contracts = (Contract.
                                                 find_contract_remaining_amount
                                                 (user))
                                    if contracts:
                                        (SalesSearchViews.
                                         show_my_contracts_remaining_amount
                                         (contracts))
                                    else:
                                        (SalesCustomerViews.
                                         all_contract_settled())
                                if choice == 6:
                                    # Search for contracts
                                    search = (MainSearch.
                                              search_all_contracts_search())
                                    contracts = (Contract.
                                                 find_contract_by_search
                                                 (search))
                                    if contracts:
                                        (MainSearch.show_all_contracts_search
                                         (contracts))
                                    else:
                                        (MainView.
                                         message_no_contract_whith_search())
                                if choice == 7:
                                    # Go back to the main menu
                                    SalesController(user)
                            else:
                                print("Please enter a number between 1 and 7!")
                        else:
                            MainView.message_no_whole_number()

                        SalesMenu.sale_contracts_menu()
                        choice = MainView.choise()

                elif choice == 3:
                    # Sales management for events
                    SalesMenu.sale_events_menu()
                    choice = MainView.choise()

                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 4:
                                if choice == 1:
                                    # Create a new event
                                    id = (ManagementEventViews.
                                          create_event_id_contract_view())
                                    contract = Contract.find_contract_by_id(id)
                                    if (user.id == contract.customer
                                            .sales_contact):
                                        if contract:
                                            if contract.contract_sign:
                                                (ManagementEventViews.
                                                 confirmation_create_event_view
                                                 (contract))
                                                response = (MainView.
                                                            oui_non_input())
                                                while True:
                                                    if response == "oui":
                                                        (title,
                                                         date_hour_start,
                                                         date_hour_end,
                                                         address, guests,
                                                         notes,
                                                         support_contact) = (
                                                            ManagementEventViews.create_event_view())
                                                        try:
                                                            (Event.
                                                             create_event
                                                             (contract, title,
                                                              date_hour_start,
                                                              date_hour_end,
                                                              address, guests,
                                                              notes,
                                                              support_contact))
                                                            (ManagementEventViews.validation_create_event_view())
                                                        except sqlalchemy.exc.OperationalError:
                                                            (SalesCustomerViews
                                                             .wrong_date_format
                                                             ())
                                                        break
                                                    if response == "non":
                                                        (ManagementEventViews.
                                                         cancelation_create_event_view())
                                                        break
                                                    else:
                                                        (MainView.
                                                         error_oui_non_input())
                                            else:
                                                (ManagementEventViews.
                                                 not_sign_contract_view
                                                 (contract))
                                        else:
                                            (ManagementEventViews.
                                             none_event_view())
                                    else:
                                        (SalesCustomerViews.
                                         not_in_charge_customer_view())
                                if choice == 2:
                                    # Show all events
                                    events = Event.find_event()
                                    if events:
                                        MainSearch.show_all_events(events)
                                    else:
                                        MainView.message_no_event()
                                if choice == 3:
                                    # Search for events
                                    search = (MainSearch.
                                              search_all_events_search())
                                    events = (Event.
                                              find_event_by_search(search))
                                    if events:
                                        (MainSearch.
                                         show_all_events_search(events))
                                    else:
                                        (MainView.message_no_event_whith_search
                                         ())
                                if choice == 4:
                                    # Go back to the main menu
                                    SalesController(user)
                            else:
                                print("Please enter a number between 1 and 4!")
                        else:
                            MainView.message_no_whole_number()

                        SalesMenu.sale_events_menu()
                        choice = MainView.choise()

                elif choice == 4:
                    # Exit the program
                    exit()
            else:
                print("Please enter a number between 1 and 4!")
        else:
            MainView.message_no_whole_number()

        SalesController(user)
        choice = MainView.choise()
