import pywinauto
from random import randrange

def click_left_button(x, y):
    '''Click left button'''
    pywinauto.mouse.click(button='left', coords=(x, y))
    pywinauto.mouse.press(button='left', coords=(x, y))
    pywinauto.mouse.release(button='left', coords=(x, y))
       
        
def main():
    for i in range(100000000000000000000):
        x = randrange(2000, 2050)
        y = randrange(1300, 1350)
        click_left_button(x, y)


if __name__ == "__main__":
    main()
