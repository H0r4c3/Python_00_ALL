

import logging

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\logging\logging_example.log'
  
#Create and configure logger
#logging.basicConfig(filename=path, format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename=path, 
                    filemode='w')

logger = logging.getLogger('main')

logging.info('Starting calculation')
a = 1
b = 2
logging.debug(f'a = {a}, b = {b}')

result = a + b  
logging.debug(f"result = {result}")
