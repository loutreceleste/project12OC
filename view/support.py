class SupportMenu:
    @staticmethod
    def support_menu(self):
        print(f"\n-----BONJOUR {self.lastname}-----")
        print("1) Menu clients.")
        print("2) Menu contrats.")
        print("3) Menu evenements.")
        print("4) Quitter la session.")
        return input("Votre choix: ")

    @staticmethod
    def support_customers_menu():
        print("\n-----MENU CLIENTS-----")
        print("1) Afficher toutes les fiches clients.")
        print("2) Retour au Menu Commercial.")
        return input("Votre choix: ")

    @staticmethod
    def support_contrats_menu():
        print("\n-----MENU CONTRATS-----")
        print("1) Afficher tout les contrats.")
        print("2) Retour au Menu Commercial.")
        return input("Votre choix: ")

    @staticmethod
    def sale_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Modifier un évènement.")
        print("2) Afficher tout les évènement.")
        print("2) Afficher tous les événements dont je suis responsable.")
        print("3) Retour au Menu Commercial.")
        return input("Votre choix: ")
