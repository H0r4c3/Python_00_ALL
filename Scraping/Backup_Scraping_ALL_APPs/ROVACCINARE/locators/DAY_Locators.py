
class DayLocators:

    # Pagina cu o zi, fiecare rand e o ora din zi

    # fiecare rand (ora)
    row_with_ore_LOCATOR = 'div.cal-hour.ng-star-inserted'
    row_with_locuri_LOCATOR = 'div.cal-event-container.cal-starts-within-day.cal-ends-within-day.ng-star-inserted'
                        
    # data zilei respective
    data1_LOCATOR = '#custom-calendar > div.calendar-header'
    data2_LOCATOR = 'div.header-bottom div.title'

    # ora randului
    ora_LOCATOR = 'div.cal-time.ng-star-inserted'

    #locuri_disponibile_LOCATOR = 'div.font-weight-600'
    locuri_disponibile_LOCATOR = 'mwl-calendar-week-view-event > div > div > div > div'

    butonul_selecteaza_LOCATOR = 'button.mat-focus-indicator.mat-raised-button.mat-button-base.mat-accent.ng-star-inserted span.mat-button-wrapper'