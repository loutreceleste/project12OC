# Epic Events - Project 12 OpenClassrooms

This repository contains the source code of a CRM system developed for Epic Events, a company specializing in organizing epic events for startups. Developed as part of a student project, this system aims to address the company's urgent need for customer relationship management (CRM). The project follows a Model-View-Controller (MVC) architecture, with Python for the backend and a flexible design to facilitate its evolution. Incorporating development and security best practices, this system is designed to improve operations and relationships with Epic Events' clients.

![Sentry Badge](https://img.shields.io/badge/Sentry-black?style=for-the-badge&logo=Sentry&logoColor=#362D59) &nbsp;&nbsp;&nbsp;&nbsp; ![Sentry Badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) &nbsp;&nbsp;&nbsp;&nbsp; ![PyCharm Badge](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white) &nbsp;&nbsp;&nbsp;&nbsp; ![PyCharm Badge](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)

## <u>Application Installation</u>

1. **Clone the repository :** To clone the repository, open a terminal window and run the following command :
    ```bash
    git clone https://github.com/loutreceleste/project12OC.git
    ```

2. **Accessing the Project Directory :** Once you have cloned the repository, navigate to the project directory using the cd command :
    ```bash
    cd project12OC
    ```

3. **Installing Required Dependencies :** The project requires several Python packages to run, to install these packages, run the following command :
    ```bash
    pip install -r requirements.txt
    ```

## <u>Database Installation</u>

Before you begin, make sure you have MySQL installed on your system. If not, you can download and install it from the official MySQL website: https://dev.mysql.com/downloads/.

1. **Connecting to MySQL :** Ensure that your MySQL server is running. Connect to MySQL using the following command in the terminal :
    ```bash
    mysql -u root -p
    ```

2. **Running the SQL script :** Once connected to MySQL, execute the provided SQL script (epicevents_database.sql). This script creates the database, tables, triggers, and a user with a password :
    ```bash
    mysql -u root -p epicevents < project12OC/epicevents_database.sql
    ```

3. **Completing the installation :** Once the SQL script has been successfully executed, you can exit the MySQL interface by typing :
    ```bash
    quit;
    ```
## <u>Launching the application</u>

To launch the application, execute the main file main.py from your terminal using the following command :
```bash
python3 main.py
```
Make sure you are in the root directory of the project before executing this command. This will launch the application and allow you to interact with it via the terminal.

## <u>Tests and Coverage</u>

1. **Tests:** Execute the following command to run all tests:

   ```bash
   pytest
   ```
   For a more detailed output, use:
   
      ```bash
      pytest -v
      ```

2. **Coverage:** To generate a coverage report type:
   ```bash
   pytest --cov=app
   ```
   To generate an HTML coverage report for the project type:
   ```bash
   pytest --cov=. --cov-report html
   ```

## <u>Flake8 Report</u>

To generate another flake8-html report please first deleate the current report "flake8_rapport" in the "project12OC" folder, then open the console, navigate through the folders of the computer in order to find yourself in the root of the "project12OC" folder and run the next command:

```bash
python3 -m flake8 --exclude=venv --format=html --htmldir=flake8_rapport
```
The report will be created with the "flake8_rapport" name.

## <u>Contribute</u>

Any contribution is welcome! Feel free to open a pull request or report any issues.

## <u>Authors</u>

Edward Peytavin https://github.com/loutreceleste

## <u>License</u>

This project is licensed under the terms of the MIT License.
