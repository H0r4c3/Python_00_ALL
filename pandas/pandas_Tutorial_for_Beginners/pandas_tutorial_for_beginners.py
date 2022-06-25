'https://www.datacamp.com/community/tutorials/pandas'

'''
REMEMBER!!!

When selecting subsets of data, square brackets [] are used.

Inside these brackets, you can use a single column/row label, a list of column/row labels, a slice of labels, a conditional expression or a colon.

Select specific rows and/or columns using loc when using the row and column names

Select specific rows and/or columns using iloc when using the positions in the table

You can assign new values to a selection based on loc/iloc.
'''

# import pandas package
import pandas as pd

# read the airbnb NYC listings csv file
path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\pandas\pandas_Tutorial_for_Beginners\listings.csv'
df_reader = pd.read_csv(path)

# display the pandas DataFrame
print("\n df_reader: \n", df_reader)

print("\n df_reader.head(): \n", df_reader.head())

print("\n df_reader.tail(): \n", df_reader.tail())

# We can select a single column using single brackets and the name of the column
# Results for a single column
print("\n df_reader['name']: \n", df_reader['name'])

# To select multiple columns at once, we use double brackets and commas between column names
# Results for multiple columns
hosts = df_reader[['host_id', 'host_name']]
print("\n Multiple column selection: \n", hosts.head())


# Show the data types for each column
print("\n Data types for each column: \n", df_reader.dtypes)

'''
To convert a column to a datetime index, we use the .to_datetime() functions (these functions exist for all supported data types like .to_string() to convert a column to be stored as a string).
We want to convert the last_review column to a datetime column
'''

# Change the type of a column to datetime
df_reader['last_review'] = pd.to_datetime(df_reader['last_review'])
print("\n Data types for each column: \n", df_reader.dtypes)


# We select the .year attribute of the newly typed datetime column, last_review, to get the year of each row.
# extract the year from a datetime series
df_reader['year'] = df_reader['last_review'].dt.year
print("\n Extract the year from a datetime series: \n",
      df_reader['year'].head())

'''
Another useful data cleaning tool is removing leading and trailing whitespace from string data. 
This can be done using the strip method.
'''

# Strip leading and trailing spaces from a string series
df_reader['name'] = df_reader['name'].str.strip()
print('\n Strip leading and trailing spaces from a string series: \n',
      df_reader['name'].head())

# Lowercase all strings in a series
df_reader['name_lower'] = df_reader['name'].str.lower()
print('\n Lowercase all strings in a series: \n',
      df_reader['name_lower'].head())

# If we want to make calculations between columns, we can easily do this by applying the operation to each of the series
# calculate using two columns
df_reader['min_revenue'] = df_reader['minimum_nights'] * df_reader['price']
print('\n Calculating the product of the minimum number of stays and the price per night: \n',
      df_reader[['minimum_nights', 'price', 'min_revenue']].head())

'''
Once the data is clean and ready to analyze, we can compute some interesting statistics to answer some business questions. 
The first question we may have is what the average and median price is for the listings in our data. 
We use the built-in .mean() and .median() methods to compute these.
'''

# get the mean price
print(df_reader['price'].mean())

# get the median price
print(df_reader['price'].median())


# get the mean grouped by type of room
print(df_reader[['room_type', 'price']].groupby(
    'room_type', as_index=False).mean())

# get the median grouped by type of room
print(df_reader[['room_type', 'price']].groupby(
    'room_type', as_index=False).median())

'''
GROUPING:
If we would like to group on additional variables, we can input a list rather than a string as the first argument of .groupby().
'''

# get the median grouped by type of room and year
print(df_reader[['room_type', 'year', 'price']].groupby(
    ['room_type', 'year'], as_index=False).median())


'''
FILTERING:
Often, we are only interested in a subset of the rows in our dataset. For example, we may only be interested in listings under $1000 as they are more common and closer to the typical listing. 
We do this by passing a Boolean expression into single brackets as shown below.
'''

# get all rows with price < 1000
df_reader_under_1000 = df_reader[df_reader['price'] < 1000]
print(df_reader_under_1000.head())

'''
We can also pass in multiple filters by surrounding each expression in parenthesis and using either & (for and expressions) or | (for or expressions). 
You will get an error if you do not surround the expressions with parentheses.
'''

# get all rows with price < 1000 and year equal to 2020
df_reader_2019_under_1000 = df_reader[(df_reader['price'] < 1000) & (df_reader['year'] == 2020)]
print(df_reader_2019_under_1000.head())


'''
Plotting
pandas also has built-in plotting capabilities. For example, we can see the distribution of prices for each listing in our dataset using a histogram in one line of code. 
Note, we use the under $1000 DataFrame here as we cannot see the bars very clearly when including all prices.
'''

# distribution of prices under $1000
ax = df_reader_under_1000['price'].plot.hist(bins=40)
