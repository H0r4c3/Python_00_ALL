'https://sparkbyexamples.com/pandas/pandas-get-cell-value-from-dataframe/'



import pandas as pd

technologies = {
     'Courses':["Spark","PySpark","Hadoop","Python","pandas"],
     'Fee' :[24000,25000,25000,24000,24000],
     'Duration':['30day','50days','55days', '40days','60days'],
     'Discount':[1000,2300,1000,1200,2500]
          }
index_labels=['r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies, index=index_labels)
print(df)

