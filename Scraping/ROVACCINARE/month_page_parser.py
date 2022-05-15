from locators.MONTH_Locators import MonthLocators


class MonthPageParser:
    """
    A class for extracting the details for every cell from month page
    """

    def __init__(self, parent):
        self.parent = parent # parent's tag = mwl-calendar-month-cell

    def __repr__(self):
        return f'\n Cells from Month Page: Day Number: {self.day_number}   |   Button: {self.day_button}   |    {self.locuri_libere}'

    @property
    def day_number(self):
        locator = MonthLocators.Day_Number_LOCATOR
        if self.parent.select_one(locator) != None:
            day_number = self.parent.select_one(locator).string
        else:
            day_number = None
        return day_number


    @property
    def day_button(self):
        locator = MonthLocators.Eye_button_LOCATOR
        if self.parent.select_one(locator) != None:
            day_button = self.parent.select_one(locator).string
            day_button = "Button OK"
        else:
            day_button = None
        return day_button

    @property
    def locuri_libere(self):
        locator = MonthLocators.Locuri_libere_LOCATOR
        if self.parent.select_one(locator) != None:
            locuri_libere = self.parent.select_one(locator).string
        else:
            locuri_libere = None
        return locuri_libere
