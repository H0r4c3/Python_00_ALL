import csv

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\modules\csv\file1.csv'

fieldnames = list()

with open(path, 'r') as input_csv:
        #fn = csv.DictReader(input_csv).fieldnames
        #fieldnames.extend(x for x in fn if x not in fieldnames)

        csv_dict = csv.DictReader(input_csv)

        for row in csv_dict:
            print(row)

        #print(fn)
        #print(fieldnames)

