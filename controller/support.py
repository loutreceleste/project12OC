from view.management import ManagementEventViews
from view.principal import MainView, MainSearch
from view.support import SupportMenu, SupportViews
from model.principal import Event


class SupportController(SupportMenu):
    def __init__(self, user):
        SupportMenu.support_menu()
        choice = MainView.choise()
        handle_support_choise(choice, user)

def handle_support_choise(choice, user):

    while True:
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                if choice == 1:
                    SupportMenu.support_customers_menu()
                    choice = MainView.choise()
                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 3:
                                if choice == 1:
                                    MainSearch.show_all_customers()
                                elif choice == 2:
                                    MainSearch.show_all_customers_search()
                                elif choice == 3:
                                    SupportController(user)
                            else:
                                print("Veuillez saisir un nombre entre 1 et 3!")
                        else:
                            MainView.message_no_whole_number()
                if choice == 2:
                    SupportMenu.support_contrats_menu()
                    choice = MainView.choise()
                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 3:
                                if choice == 1:
                                    MainSearch.show_all_contracts()
                                elif choice == 2:
                                    MainSearch.show_all_contracts_search()
                                elif choice == 3:
                                    SupportController(user)
                            else:
                                print("Veuillez saisir un nombre entre 1 et 3!")
                        else:
                            MainView.message_no_whole_number()
                if choice == 3:
                    while True:
                        SupportMenu.support_events_menu()
                        choice = MainView.choise()
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 5:
                                if choice == 1:
                                    id = ManagementEventViews.update_event_id_contract_view()
                                    event = Event.find_event(id)
                                    if event.support_contact == user.name_lastname:
                                        if event:
                                            title, date_hour_start, date_hour_end, address, guests, notes = (
                                                ManagementEventViews.update_event_view(event, id))
                                            Event.update_event_for_support(title, date_hour_start, date_hour_end,
                                                                           address, guests, notes, event)
                                            ManagementEventViews.validation_update_event_view()
                                        else:
                                            ManagementEventViews.none_event_view()
                                    else:
                                        ManagementEventViews.not_in_charge_event_view()
                                elif choice == 2:
                                    MainSearch.show_all_events()
                                elif choice == 3:
                                    events = Event.find_event_by_support(user)
                                    if events:
                                        SupportViews.show_all_events_self_support(events)
                                    else:
                                        SupportViews.not_assigned_event()
                                elif choice == 4:
                                    MainSearch.show_all_events_search()
                                elif choice == 5:
                                    SupportController(user)
                            else:
                                print("Veuillez saisir un nombre entre 1 et 5!")
                        else:
                            MainView.message_no_whole_number()
                if choice == 4:
                    exit()
            else:
                print("Veuillez saisir un nombre entre 1 et 4!")
        else:
            MainView.message_no_whole_number()

        SupportController(user)
        choice = MainView.choise()
