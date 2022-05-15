'https://medium.com/@ageitgey/quick-tip-the-easiest-way-to-grab-data-out-of-a-web-page-in-python-7153cecfca58'

import pandas as pd

# Pandas will find any significant html tables on the page and return each one as a new DataFrame object.

calls_df, = pd.read_html("http://apps.sandiego.gov/sdfiredispatch/", header=0, parse_dates=["Call Date"])

print(calls_df)

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Scraping\Scrape_Tabular_Data_from_html_Pages\calls.csv'
calls_df.to_csv(path, index=False)