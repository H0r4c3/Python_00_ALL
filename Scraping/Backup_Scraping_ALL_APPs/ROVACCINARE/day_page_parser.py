from bs4 import BeautifulSoup
from locators.DAY_Locators import DayLocators


class DayPageParser:
    """
    Pagina cu o zi (pentru fiecare celula/zi, din pagina cu calendarul pentru o luna), fiecare rand e o ora din zi
    """

    def __init__(self, parent):
        self.parent = parent # parent's tag = mwl-calendar-month-cell

    def __repr__(self):
        return f'\n Rows in Day page: Data: {self.data}  |  Ora: {self.ora}  |  Locuri disponibile: {self.locuri_disponibile}  |  Butonul "Selecteaza": {self.butonul_selecteaza}'

    @property
    def data(self):
        locator = DayLocators.data2_LOCATOR
        if self.parent.select_one(locator) != None:
            item_data = self.parent.select_one(locator).string
        else:
            item_data = None
        return item_data

    @property
    def ora(self):
        locator = DayLocators.ora_LOCATOR
        if self.parent.select_one(locator) != None:
            item_ora = self.parent.select_one(locator).string
        else:
            item_ora = None
        return item_ora

    @property
    def locuri_disponibile(self):
        locator = DayLocators.locuri_disponibile_LOCATOR
        if self.parent.select_one(locator) != None:
            item_locuri_disponibile = self.parent.select_one(locator).string
        else:
            item_locuri_disponibile = None
        return item_locuri_disponibile

    @property
    def butonul_selecteaza(self):
        locator = DayLocators.butonul_selecteaza_LOCATOR
        if self.parent.select_one(locator) != None:
            item_butonul_selecteaza = self.parent.select_one(locator).text
            item_butonul_selecteaza = item_butonul_selecteaza.strip(" edit")
        else:
            item_butonul_selecteaza = None
        return item_butonul_selecteaza
