from database import session
from model.principal import check_date_format

class ManagementMenu:
    @staticmethod
    def management_menu():
        print(f"\n-----MENU GESTION-----")
        print("1) Menu collaborateurs.")
        print("2) Menu clients.")
        print("3) Menu contrats.")
        print("4) Menu evenements.")
        print("5) Quitter la session.")

    @staticmethod
    def management_users_menu():
        print("\n-----MENU COLLABORATEURS-----")
        print("1) Créer un collaborateur.")
        print("2) Modifier un collaborateur.")
        print("3) Supprimer un collaborateur.")
        print("4) Rechercher un collaborateur.")
        print("5) Afficher tout les collaborateurs.")
        print("6) Retour au Menu Gestion.")

    @staticmethod
    def management_customers_menu():
        print("\n-----MENU CLIENTS-----")
        print("1) Afficher toutes les fiches clients.")
        print("2) Rechercher un client.")
        print("3) Retour au Menu Gestion.")

    @staticmethod
    def management_contrats_menu():
        print("\n-----MENU CONTRATS-----")
        print("1) Créer un contrat.")
        print("2) Modifier un contrat.")
        print("3) Afficher tout les contrats.")
        print("4) Rechercher un contrat.")
        print("5) Retour au Menu Gestion.")

    @staticmethod
    def management_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Modifier un évènement.")
        print("2) Afficher tout les évènement.")
        print("3) Rechercher un évènement.")
        print("4) Afficher tous les événements sans supports associés.")
        print("5) Retour au Menu Gestion.")

class ManagmentSearchViews:

    @staticmethod
    def show_all_events_no_support(events):
        print("\n---TOUS LES EVENEMENTS SANS SUPPORT ASSOCIE---")
        for event in events:
            print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                  f"Prénom et nom du client: {event.contract.customer.name_lastname}, "
                  f"Email du client: {event.contract.customer.email}, "
                  f"Téléphone du client: {event.contract.customer.phone}, "
                  f"Nom de l'événement: {event.title}, Date de début: {event.date_hour_start}, "
                  f"Date de fin: {event.date_hour_end}, Adresse: {event.address}, "
                  f"Nombre de convives: {event.guests}, Notes: {event.notes}, "
                  f"Support associé: {event.user.name_lastname if event.user else 'Aucun support'}")

class ManagementUserViews:

    @staticmethod
    def create_user_view():
        print("\n-----NOUVEAU COLLABORATEUR-----")
        name_lastname = input("Nom et prénom: ")
        while not name_lastname.strip():
            print("Le nom et prénom ne peuvent pas être vides.")
            name_lastname = input("Nom et prénom: ")
        print("\n-----LES DEPARTEMENTS A RESEIGNER:-----")
        print("-----COM: COMMERCIAL-----")
        print("-----GES: GESTION-----")
        print("-----SUP: SUPPORT-----")
        while True:
            department = input("Département: ").upper()
            if department in ('COM', 'GES', 'SUP'):
                break
            else:
                print("Département invalide. Veuillez choisir parmi 'COM', 'GES' ou 'SUP'.")
        password = input("Mot de passe: ")
        email = input("Email: ")
        return name_lastname, department, password, email

    @staticmethod
    def validation_user_creation(name_lastname):
        print(f"Le collaborateur {name_lastname} a été créé avec succès!")

    @staticmethod
    def delete_user_id_view():
        print("Quel collaborateur souhaitez-vous supprimer?")
        id = input("ID du collaborateur: ")
        return id

    @staticmethod
    def confirmation_delete_user_view(user):
        print(f"Êtes-vous sûr de vouloir effacer le collaborateur {user.name_lastname}?")

    @staticmethod
    def validation_delete_user_view(user):
        print(f"{user.name_lastname} a bien été supprimée de la base de données.")

    @staticmethod
    def cancelation_delete_user_view():
        print("Suppression annulée.")

    @staticmethod
    def none_user_view():
        print("Erreur de frappe ou aucun collaborateur ne correspond a cette ID.")

    @staticmethod
    def update_user_id_view():
        print("Quel collaborateur souhaitez-vous modifier?")
        id = input("ID du collaborateur: ")
        return id

    @staticmethod
    def update_user_view(user, id):
        print(f"\n-----MISE A JOUR DU COLLABORATEUR N°{id}-----")
        print("Appuyez sur 'Entrée' afin de conserver l'information actuelle.")
        name_lastname = input(f"Nom et prénom ({user.name_lastname}): ")
        print("\n-----LES DEPARTEMENTS A RESEIGNER:-----")
        print("-----COM: COMMERCIAL-----")
        print("-----GES: GESTION-----")
        print("-----SUP: SUPPORT-----")
        department = input(f"Departement ({user.department}): ").upper()
        password = input("Mot de passe (laissez vide pour ne pas modifier): ")
        email = input(f"Email ({user.email}): ")
        return name_lastname, department, password, email

    @staticmethod
    def validation_update_user_view(user):
        print(f"Le collaborateur {user.name_lastname} a bien ete modifié")

class ManagementContractViews:

    @staticmethod
    def create_contract_id_customer_view():
        print("À partir de quel client souhaitez-vous créer un contrat?")
        id = input("ID du client: ")
        return id

    @staticmethod
    def create_contract_view():
        print("\n-----NOUVEAU CONTRAT-----")
        while True:
            total_amount = input(f"Cout total du contrat: ")
            if total_amount.isdigit():
                total_amount = int(total_amount)
                break
            else:
                print("Veuillez indiquer un nombre entier.")
        while True:
            settled_amount = input("Montant déjà réglé: ")
            if settled_amount.isdigit():
                settled_amount = int(settled_amount)
                break
            else:
                print("Veuillez indiquer un nombre entier.")
        while True:
            contract_sign_input = input("Le contrat a-t-il été validé par le client? (Oui=True / Non=False): ").lower()
            if contract_sign_input in ('true', 'false'):
                contract_sign = contract_sign_input == 'true'
                break
            else:
                print('Veuillez répondre par "True" ou par "False"')
        return total_amount, settled_amount, contract_sign

    @staticmethod
    def validation_create_contract_view():
        print("Votre contrat a été créé avec succès!")

    @staticmethod
    def cancelation_create_contract_view():
        print("Création annulée.")

    @staticmethod
    def none_customer_view():
        print("Erreur de frappe ou aucun client ne correspond a cette ID.")

    @staticmethod
    def confirmation_create_contract_view(customer):
        print(f"Souhaitez-vous créer un contrat pour le client {customer.name_lastname}?")

    @staticmethod
    def update_contract_id_view():
        print("Quel contrat souhaitez-vous modifier?")
        id = input("ID du contrat: ")
        return id

    @staticmethod
    def update_contract_view(contract, id):
        print(f"\n-----MISE A JOUR DU CONTRAT N°{id}-----")
        print("Appuyez sur 'Entrée' afin de conserver l'information actuelle.")

        total_amount = None
        settled_amount = None
        contract_sign = None

        new_total_amount = input(f"Coût total du contrat ({contract.total_amount}): ")
        if new_total_amount.strip() != '':
            while True:
                if new_total_amount.isdigit():
                    total_amount = int(new_total_amount)
                    break
                else:
                    print("Veuillez indiquer un nombre entier valide.")
                    new_total_amount = input(f"Coût total du contrat ({contract.total_amount}): ")
        new_settled_amount = input(f"Montant déjà réglé ({contract.settled_amount}): ")
        if new_settled_amount.strip() != '':
            while True:
                if new_settled_amount.isdigit():
                    settled_amount = int(new_settled_amount)
                    break
                else:
                    print("Veuillez indiquer un nombre entier valide.")
                    new_settled_amount = input(f"Montant déjà réglé ({contract.settled_amount}): ")
        new_contract_sign_input = input("Le contrat a-t-il été validé par le client? (Oui=True / Non=False): ").lower()
        if new_contract_sign_input.strip() != '':
            while True:
                if new_contract_sign_input in ('true', 'false'):
                    contract_sign = new_contract_sign_input == 'true'
                    break
                else:
                    print('Veuillez répondre par "True" ou par "False"')
                    new_contract_sign_input = input(
                        "Le contrat a-t-il été validé par le client? (Oui=True / Non=False): ").lower()

        return total_amount, settled_amount, contract_sign

    @staticmethod
    def validation_update_contract_view():
        print("Votre contrat a été modifiée avec succès!")

    @staticmethod
    def none_contract_view():
        print("Erreur de frappe ou aucun contrat ne correspond a cette ID.")

    @staticmethod
    def not_in_charge_contract_view():
        print("Vous n'êtes pas en charge de ce contrat.")

class ManagementEventViews:

    @staticmethod
    def create_event_id_contract_view():
        print("À partir de quel contrat souhaitez-vous créer un événement?")
        id = input("ID du contrat: ")
        return id

    @staticmethod
    def confirmation_create_event_view(contrat):
        print(f"Souhaitez vous créer un événement pour le client {contrat.customer.name_lastname} à partir du "
              f"contrat n°{contrat.id}?")

    @staticmethod
    def create_event_view():
        print("\n-----NOUVEL EVENEMENT-----")
        title = input(f"Nom de l'événement: ")
        while True:
            date_hour_start = input(f"Date et heure du début de l'événement (format AAAA-MM-JJ HH:MM:SS): ")
            if check_date_format(date_hour_start):
                break
            else:
                print("Format invalide. Veuillez saisir la date et l'heure au format AAAA-MM-JJ HH:MM:SS.")
        while True:
            date_hour_end = input(f"Date et heure de fin de l'événement (format AAAA-MM-JJ HH:MM:SS): ")
            if check_date_format(date_hour_end):
                break
            else:
                print(
                    "Format invalide. Veuillez saisir la date et l'heure au format AAAA-MM-JJ HH:MM:SS.")
        address = input(f"Adresse de l'événement: ")
        while True:
            guests = input(f"Nombre d'invitées: ")
            if guests.isdigit():
                break
            else:
                print("Veuillez indiquer un nombre entier.")
        notes = input(f"Notes: ")
        support_contact = None
        return title, date_hour_start, date_hour_end, address, guests, notes, support_contact

    @staticmethod
    def validation_create_event_view():
        print("Votre événement a été créé avec succès!")

    @staticmethod
    def cancelation_create_event_view():
        print("Création annulée.")

    @staticmethod
    def not_sign_contract_view(contrat):
        print(f"Le contrat n°{contrat.id} n'a pas été signé par le client. Veuillez vous rapprocher de ce "
              f"dernier.")

    @staticmethod
    def none_event_view():
        print("Erreur de frappe ou aucun contrat ne correspond a cette ID.")

    @staticmethod
    def update_event_id_contract_view():
        print("Quel événement souhaitez-vous modifier?")
        id = input("ID de l'événement: ")
        return id

    @staticmethod
    def update_event_view(event, id):
        from model.principal import User

        support_id = None

        print(f"\n-----MISE A JOUR DE L'ÉVÉNEMENT N°{id}-----")
        title = input(f"Nom de l'événement: {event.title}")
        while True:
            date_hour_start_input = input(f"Date et heure du début de l'événement (format AAAA-MM-JJ HH:MM:SS) "
                                          f"({event.date_hour_start}): ")
            if date_hour_start_input.strip() != '':
                if check_date_format(date_hour_start_input):
                    date_hour_start = date_hour_start_input
                    break
                else:
                    print("Format invalide. Veuillez saisir la date et l'heure au format AAAA-MM-JJ HH:MM:SS.")
            else:
                date_hour_start = event.date_hour_start
                break
        while True:
            date_hour_end_input = input(f"Date et heure de fin de l'événement (format AAAA-MM-JJ HH:MM:SS) "
                                        f"({event.date_hour_end}): ")
            if date_hour_end_input.strip() != '':
                if check_date_format(date_hour_end_input):
                    date_hour_end = date_hour_end_input
                    break
                else:
                    print("Format invalide. Veuillez saisir la date et l'heure au format AAAA-MM-JJ HH:MM:SS.")
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
        while True:
            support_contact = input(f"Support référent (Nom et prénom) ({event.support_contact}): ")
            if support_contact is None:
                break
            support = session.query(User).filter(User.name_lastname == support_contact).first()

            if support and support.department == "SUP":
                print(f"Souhaitez vous assigner {support.name_lastname} a l'événement?")
                response = input("Oui ou Non?").strip().lower()
                if response == "oui":
                    support_id = support.id
                    break
                if response == "non":
                    print("Merci de renseigner le nom et le prénom d'un support à assigner à l'événement.")
                else:
                    print("Erreur de frappe. Veuillez répondre par 'Oui' ou 'Non'.")
            else:
                print('Collaborateur inconnu de la base de données ou non attribué a la section "support". '
                      "Merci de renseigner le nom et le prénom d'un collaborateur à assigner à l'événement.")
        return title, date_hour_start, date_hour_end, address, guests, notes, support_id

    @staticmethod
    def validation_update_event_view():
        print("L'événement a été correctement modifié!")

    @staticmethod
    def not_in_charge_event_view():
        print("Vous n'êtes pas en change de cette événement.")

    @staticmethod
    def all_event_assigned():
        print("Tous les événements ont l'air d'avoir été attribuées.")
