# This class is used to display different menus for the support module
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
                  f"Client associé: {event.event_customer_id}, "
                  f"Support associé: {event.event_support_id}, "
                  f"Nom de l'événement: {event.event_title}, "
                  f"Date de début: {event.event_date_start}, "
                  f"Date de fin: {event.event_date_end}, "
                  f"Adresse: {event.event_adress}, "
                  f"Nombre de convives: {event.event_guests}, "
                  f"Notes: {event.event_notes}")

    # This method displays a message when the current user is not responsible
    # for any events
    @staticmethod
    def not_assigned_event():
        print("Vous ne semblez être responsable d'aucun événement.")
