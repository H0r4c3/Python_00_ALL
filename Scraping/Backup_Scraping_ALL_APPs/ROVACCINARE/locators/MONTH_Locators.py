class MonthLocators:
    # pagina cu calendarul pentru o luna, fiecare celula e o zi: 
    #Calendar_Month_Cell_LOCATOR = '#custom-calendar > div:nth-child(2) > mwl-calendar-month-view > div > div > div:nth-child(1) > div > mwl-calendar-month-cell'
    Calendar_Month_Cell_LOCATOR = 'div.cal-days mwl-calendar-month-cell.cal-cell.cal-day-cell.cal-future.cal-in-month.ng-star-inserted'

    Day_Number_LOCATOR = 'div.cal-day-number.m-4'

    #Eye_button_LOCATOR = '#custom-calendar > div:nth-child(2) > mwl-calendar-month-view > div > div > div:nth-child(1) > div > mwl-calendar-month-cell:nth-child(6) > div > button'
    Eye_button_LOCATOR = 'div > button > span.mat-button-wrapper'

    Locuri_libere_LOCATOR = '#custom-calendar > div > mwl-calendar-month-view > div > div > div > div > mwl-calendar-month-cell > div > div.font-weight-600.mt-16.ng-star-inserted'