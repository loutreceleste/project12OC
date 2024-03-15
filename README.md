# project12OC
## Installation de la base de données "epicevents"

Ce guide explique comment installer la base de données "epicevents" à l'aide de MySQL.

### Prérequis

Avant de commencer, assurez-vous d'avoir installé MySQL sur votre système. Si ce n'est pas le cas, vous pouvez le télécharger et l'installer à partir du site officiel de MySQL : [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/).

### Installation de la base de données

1. **Connexion à MySQL :** Assurez-vous que votre serveur MySQL est en cours d'exécution. Connectez-vous à MySQL à l'aide de la commande suivante :
    ```
    mysql -u root -p
    ```

2. **Exécution du script SQL :** Une fois connecté à MySQL, exécutez le script SQL fourni (`epicevents_database.sql`). Ce script crée la base de données, les tables, les déclencheurs, et un utilisateur avec un mot de passe.
    ```
    mysql -u root -p epicevents < chemin_vers_le_fichier/epicevents_database.sql
    ```

3. **Terminer l'installation :** Une fois le script SQL exécuté avec succès, vous pouvez quitter l'interface MySQL en tapant :
    ```
    quit;
    ```

