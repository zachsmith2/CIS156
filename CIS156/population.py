# Zachary Smith
# PA_12

import pandas as pd

list_of_countries_needed = ['Year','Bosnia', 'Georgia', 'Ireland', 'Lithuania', 'Norway', 'Slovakia' ]

path = input("Enter the path to the CSV file you wish to read: ")
filename = input("Enter the file name: ")
beginning_year = int(input("Enter the beginning year: "))
ending_year = int(input("Enter the ending year: "))

df =pd.read_csv(path+ "\"+ C:\CIS156\PA12)
new_df = df[list_of_countries_needed]

new_df.set_index("Year",inplace =True)
dataframe_from_beginning_year_to_ending_year = new_df.loc[beginning_year:ending_year]

population_string = "Population from {0} to {1}".format(beginning_year,ending_year)

import seaborn as sns
import matplotlib.pyplot as plt

plot = sns.lineplot(data=dataframe_from_beginning_year_to_ending_year)
plot.set(ylabel = 'Population ',xlabel = 'Year')
plot.set_title(population_string)
plot.legend(loc="upper left")

plt.figure(figsize=(30,5))
