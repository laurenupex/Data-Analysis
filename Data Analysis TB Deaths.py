from pandas import *

data = read_excel(r"path file")  # imports excel data (replace path file with path of WHO POP TB all in same repository
print(data)  # prints table from excel

popColumn = data["Population (1000s)"]  # assigns data in population column to variable
print("The total population of all countries is", popColumn.sum())  # calculates sum of populations
print("The smallest population is", popColumn.min())  # prints the smallest population size
print("The largest population is", popColumn.max())  # prints the largest population size
print("The mean population is", popColumn.mean())  # prints the mean population size
print("The median population size is", popColumn.median())  # prints the median population size
print("The range in population size is", popColumn.max() - popColumn.min())  # prints the range of population size

deathsColumn = data["TB deaths"]  # assigns data in TB deaths column to variable
print("The total deaths of all countries is", deathsColumn.sum())  # calculates sum of deaths
print("The smallest amount of deaths is", deathsColumn.min())  # prints the smallest number of deaths
print("The largest amount of deaths is", deathsColumn.max())  # prints the largest number of deaths
print("The mean number of deaths is", deathsColumn.mean())  # prints the mean number of deaths
print("The median number of deaths is", deathsColumn.median())  # prints the median number of deaths
print("The range in number of deaths is", deathsColumn.max() - deathsColumn.min())  # prints the range of number of
# deaths

deathRateColumn = deathsColumn * 100 / popColumn  # calculates death rate for each row
data["TB deaths (per 100,000)"] = deathRateColumn  # adds death rate to table
print(data)

print(data.sort_values("TB deaths (per 100,000)"))  # sorts table in order of death rate
