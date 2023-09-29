'''
Created on Mar 27, 2020

@author: Horace.000
'''

import time
import sys
import timeit

from random import randrange

#set PYTHONPATH=%PYTHONPATH%;C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\

sys.path.append(r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Controlling_the_Keyboard_and_Mouse\Neverwinter')

#for item in sys.path:
#    print(item)

#from craft_button_module import craft_button_function
#from collect_results_button_module import collect_results_button_function
#from message_box_module import message_box_function

from functions_package.craft_button_module import craft_button_function
from functions_package.collect_results_button_module import collect_results_button_function
from functions_package.message_box_module import message_box_function



time.sleep(5)

starttime = timeit.default_timer()

for i in range(0, 1500000000):
    xcraftrand = randrange(2046, 2048)
    ycraftrand = randrange(1370, 1372)
    craft_button_function(xcraftrand, ycraftrand)
    #print("xcraftrand = ", xcraftrand, "ycraftrand = ", ycraftrand)
    
    time.sleep(1)
    
    xcollectrand = randrange(1920, 1922)
    ycollectrand = randrange(1264, 1266)
    collect_results_button_function(xcollectrand, ycollectrand)
    #print("xcollectrand = ", xcollectrand, "ycollectrand = ", ycollectrand)

duration_seconds = timeit.default_timer() - starttime
duration_minutes = duration_seconds / 60
MESSAGE_PROFESSION = str(i) + " repetitions done " + "in " + str(round(duration_seconds, 2)) + " seconds " + "(" + str(round(duration_minutes, 2)) + " minutes" + ")"

print(MESSAGE_PROFESSION)

message_box_function(MESSAGE_PROFESSION)
