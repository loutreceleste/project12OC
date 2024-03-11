from database import session


class SupportMenu:
    @staticmethod
    def support_menu():
        print(f"\n-----MENU SUPPORT-----")
        print("1) Menu clients.")
        print("2) Menu contrats.")
        print("3) Menu evenements.")
        print("4) Quitter la session.")

    @staticmethod
    def support_customers_menu():
        print("\n-----MENU CLIENTS-----")
        print("1) Afficher toutes les fiches clients.")
        print("2) Rechercher un client.")
        print("3) Retour au Menu Support.")

    @staticmethod
    def support_contrats_menu():
        print("\n-----MENU CONTRATS-----")
        print("1) Afficher tout les contrats.")
        print("2) Rechercher un contrat.")
        print("3) Retour au Menu Support.")

    @staticmethod
    def support_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Modifier un évènement.")
        print("2) Afficher tout les évènement.")
        print("3) Afficher tous les événements dont je suis responsable.")
        print("4) Rechercher un évènement.")
        print("5) Retour au Menu Support.")

    @staticmethod
    def show_all_events_self_support(user):
        from model.principal import Event
        print("\n---TOUS LES EVENEMENTS DONT JE SUIS RESPONSABLE---")
        events = session.query(Event).filter(Event.support_contact == user.name_lastname).all()
        if events:
            for event in events:
                print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                      f"Client associé: {event.event_customer_id}, Support associé: {event.event_support_id}, "
                      f"Nom de l'événement: {event.event_title}, Date de début: {event.event_date_start}, "
                      f"Date de fin: {event.event_date_end}, Adresse: {event.event_adress}, "
                      f"Nombre de convives: {event.event_guests}, Notes: {event.event_notes}")
        else:
            print("Vous ne semblez être responsable d'aucun événement.")
