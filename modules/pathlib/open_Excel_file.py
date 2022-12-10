'https://www.codegrepper.com/code-examples/python/how+to+open+excel+with+python'

import os
from pathlib import Path
# opening EXCEL through Code
#local path in dir
my_path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\pathlib\my_Excel.xlsx'
absolutePath = Path(my_path).resolve()
os.system(f'Start excel.exe "{absolutePath}"')