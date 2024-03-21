# This class is used to display different menus for the support module
from model.principal import check_date_format


class SupportMenu:
    # This method displays the main support menu
    @staticmethod
    def support_menu():
        print("\n-----MENU SUPPORT-----")
        print("1) Menu clients.")
        print("2) Menu contrats.")
        print("3) Menu evenements.")
        print("4) Quitter la session.")

    # This method displays the customers sub-menu
    @staticmethod
    def support_customers_menu():
        print("\n-----MENU CLIENTS-----")
        print("1) Afficher toutes les fiches clients.")
        print("2) Rechercher un client.")
        print("3) Retour au Menu Support.")

    # This method displays the contracts sub-menu
    @staticmethod
    def support_contrats_menu():
        print("\n-----MENU CONTRATS-----")
        print("1) Afficher tout les contrats.")
        print("2) Rechercher un contrat.")
        print("3) Retour au Menu Support.")

    # This method displays the events sub-menu
    @staticmethod
    def support_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Modifier un évènement.")
        print("2) Afficher tout les évènement.")
        print("3) Afficher tous les événements dont je suis responsable.")
        print("4) Rechercher un évènement.")
        print("5) Retour au Menu Support.")


# This class is used to display different views for the support module
class SupportViews:
    # This method displays all events that the current user is responsible for
    @staticmethod
    def show_all_events_self_support(events):
        print("\n---TOUS LES EVENEMENTS DONT JE SUIS RESPONSABLE---")
        for event in events:
            print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                  f"Prénom et nom du client: "
                  f"{event.contract.customer.name_lastname}, "
                  f"Email du client: {event.contract.customer.email}, "
                  f"Téléphone du client: {event.contract.customer.phone}, "
                  f"Nom de l'événement: {event.title}, "
                  f"Date de début: {event.date_hour_start}, "
                  f"Date de fin: {event.date_hour_end}, "
                  f"Adresse: {event.address}, "
                  f"Nombre de convives: {event.guests}, Notes: {event.notes}, "
                  f"Support associé: "
                  f"{event.user.name_lastname if event.user else 'Aucun'}")

    @staticmethod
    def update_event_view_support(event, id):

        print(f"\n-----MISE A JOUR DE L'ÉVÉNEMENT N°{id}-----")
        print("Appuyez sur 'Entrée' afin de conserver l'information actuelle.")
        title = input(f"Nom de l'événement ({event.title}): ")
        while True:
            date_hour_start_input = input(f"Date et heure du début de "
                                          f"l'événement (format AAAA-MM-JJ "
                                          f"HH:MM:SS) "
                                          f"({event.date_hour_start}): ")
            if date_hour_start_input.strip() != '':
                if check_date_format(date_hour_start_input):
                    date_hour_start = date_hour_start_input
                    break
                else:
                    print("Format invalide. Veuillez saisir la date et "
                          "l'heure au format AAAA-MM-JJ HH:MM:SS.")
            else:
                date_hour_start = event.date_hour_start
                break
        while True:
            date_hour_end_input = input(f"Date et heure de fin de l'événement "
                                        f"(format AAAA-MM-JJ HH:MM:SS) "
                                        f"({event.date_hour_end}): ")
            if date_hour_end_input.strip() != '':
                if check_date_format(date_hour_end_input):
                    date_hour_end = date_hour_end_input
                    break
                else:
                    print("Format invalide. Veuillez saisir la date et l'heure"
                          " au format AAAA-MM-JJ HH:MM:SS.")
            else:
                date_hour_end = event.date_hour_end
                break
        address = input(f"Adresse de l'événement ({event.address}): ")
        while True:
            guests_input = input(f"Nombre d'invités ({event.guests}): ")
            if guests_input.strip() != '':
                if guests_input.isdigit():
                    guests = int(guests_input)
                    break
                else:
                    print("Veuillez indiquer un nombre entier.")
            else:
                guests = event.guests
                break
        notes = input(f"Notes ({event.notes}): ")
        return title, date_hour_start, date_hour_end, address, guests, notes

    # This method displays a message when the current user is not responsible
    # for any events
    @staticmethod
    def not_assigned_event():
        print("Vous ne semblez être responsable d'aucun événement.")
