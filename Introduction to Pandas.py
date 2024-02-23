from pandas import *

data = read_excel(r"path file")  # retrieves data from excel file (replace "path file" with path of WHO POP TB some in
# same repository
print(data)  # prints table

tbColumn = data["TB deaths"]  # assigns one column of data to a variable
print("The total number of TB deaths is", tbColumn.sum())  # total number in column
print("The minimum number of TB deaths per country is", tbColumn.min())  # minimum value in column
print("The maximum number of TB deaths per country is", tbColumn.max())  # maximum value in column
print("The average number of TB deaths per country is", tbColumn.sum()/12, "or", tbColumn.median())  # average by mean
# and median in column

popColumn = data["Population (1000s)"]  # assigns population column to variable
print("The total population is", popColumn.sum())  # total number in column
print("The minimum population is", popColumn.min())  # minimum value in column
print("The maximum population is", popColumn.max())  # maximum value in column
print("The average population is", popColumn.sum()/12, "or", popColumn.median())  # average by mean
# and median in column

print(data.sort_values("TB deaths"))  # sorts rows in table in order of TB deaths column
print(data)  # sort by column values doesn't override order of original data
print(data.sort_values("Country"))  # for strings, will sort in alphabetical order
print(data.sort_values("Population (1000s)"))

rateColumn = tbColumn * 100 / popColumn  # will reiterate for each row to calculate death rate
print(rateColumn)  # prints column as standalone
data["TB deaths (per 100,000)"] = rateColumn  # adds column to original table
print(data)
