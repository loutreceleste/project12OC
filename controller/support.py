from view.management import ManagementEventViews
from view.principal import MainView, MainSearch
from view.support import SupportMenu, SupportViews
from model.principal import Event, Customer, Contract


class SupportController(SupportMenu):
    def __init__(self, user):
        # Display the support menu
        SupportMenu.support_menu()
        # Get user's choice
        choice = MainView.choise()
        # Handle user's support choice
        handle_support_choice(choice, user)


def handle_support_choice(choice, user):

    while True:
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                if choice == 1:
                    # Support management for customers
                    SupportMenu.support_customers_menu()
                    choice = MainView.choise()
                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 3:
                                if choice == 1:
                                    # Show all customers
                                    customers = Customer.find_customer()
                                    if customers:
                                        (MainSearch.
                                         show_all_customers(customers))
                                    else:
                                        MainView.message_no_customer()
                                elif choice == 2:
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
                                elif choice == 3:
                                    # Go back to the main menu
                                    SupportController(user)
                            else:
                                print("Please enter a number between 1 and 3!")
                        else:
                            MainView.message_no_whole_number()
                if choice == 2:
                    # Support management for contracts
                    SupportMenu.support_contrats_menu()
                    choice = MainView.choise()
                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 3:
                                if choice == 1:
                                    # Show all contracts
                                    contracts = Contract.find_contract()
                                    if contracts:
                                        (MainSearch.show_all_contracts
                                         (contracts))
                                    else:
                                        MainView.message_no_contract()
                                elif choice == 2:
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
                                elif choice == 3:
                                    # Go back to the main menu
                                    SupportController(user)
                            else:
                                print("Please enter a number between 1 and 3!")
                        else:
                            MainView.message_no_whole_number()
                if choice == 3:
                    while True:
                        # Support management for events
                        SupportMenu.support_events_menu()
                        choice = MainView.choise()
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 5:
                                if choice == 1:
                                    # Update an existing event
                                    id = (ManagementEventViews.
                                          update_event_id_contract_view())
                                    event = Event.find_event_by_id(id)
                                    print(event)
                                    if (event.support_contact ==
                                            user.id):
                                        if event:
                                            (title, date_hour_start,
                                             date_hour_end, address, guests,
                                             notes) = (
                                                SupportViews.
                                                update_event_view_support
                                                (event, id))
                                            Event.update_event_for_support(
                                                event, title, date_hour_start,
                                                date_hour_end, address, guests,
                                                notes)
                                            (ManagementEventViews.
                                             validation_update_event_view())
                                        else:
                                            (ManagementEventViews.
                                             none_event_view())
                                    else:
                                        (ManagementEventViews.
                                         not_in_charge_event_view())
                                elif choice == 2:
                                    # Show all events
                                    events = Event.find_event()
                                    if events:
                                        MainSearch.show_all_events(events)
                                    else:
                                        MainView.message_no_event()
                                elif choice == 3:
                                    # Show events assigned to the current
                                    # support
                                    events = Event.find_event_by_support(user)
                                    if events:
                                        (SupportViews.
                                         show_all_events_self_support(events))
                                    else:
                                        SupportViews.not_assigned_event()
                                elif choice == 4:
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
                                elif choice == 5:
                                    # Go back to the main menu
                                    SupportController(user)
                            else:
                                print("Please enter a number between 1 and 5!")
                        else:
                            MainView.message_no_whole_number()
                if choice == 4:
                    # Exit the program
                    exit()
            else:
                print("Please enter a number between 1 and 4!")
        else:
            MainView.message_no_whole_number()

        SupportController(user)
        choice = MainView.choise()
