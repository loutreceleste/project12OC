from view.sales import SalesMenu
from view.principal import MainView

class SalesController(SalesMenu):
    def __init__(self):
        SalesMenu.sale_menu()
        choice = MainView.choise()
        handle_sales_choise(choice)

def handle_sales_choise(choice):
    if choice == '1':

