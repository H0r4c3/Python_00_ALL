'https://medium.com/python-in-plain-english/10-automation-scripts-for-your-daily-python-projects-892a82be3f75'

from openpyxl import load_workbook

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\openpyxl\test.xlsx'

wb = load_workbook(path)

sheet = wb.active
# Read by Rows
for row in sheet.rows:
    for cell in row:
        print(cell.value, end=' ')
    print()
    
# Read by Column
for col in sheet.columns:
    for cell in col:
        print(cell.value, end=' ')
    print()
    
# Read Specific Column
for col in sheet['A']:
    print(col.value)
    
# Read Specific Cell
# method 1
print(sheet['A1'].value)
# method 2 
data = sheet.cell(row=1, column=1).value
print(data)

# Writing and Saving Excel
sheet.cell(row=1, column=1).value = 'Hello World'
wb.save(path)