import numpy as np
import pandas as pd
from pandas import read_csv
from pandas import read_excel
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


'''
Using ChatGPT, a code was generated to load CSV and XLS files for the data.
'''

# Load an Excel file
xls_file_path = "C:/Users/Flopa/Documents/Engineering/Engineering 2nd year/ENDG 310/Labs/lab 2/data/NFDB_point_stats.xlsx"
data_xls = pd.read_excel(xls_file_path, sheet_name='NFDB_Summary_Stats', skiprows=4)  # Make sure to specify the correct file and sheet name

# Display the data (use .head() to display the first few rows)
print(data_xls.head())

# Load a CSV file
csv_file_path = "C:/Users/Flopa/Documents/Engineering/Engineering 2nd year/ENDG 310/Labs/lab 2/data/co2_data.csv"
data_csv = pd.read_csv(csv_file_path, skiprows = 40)

# Display the data (use .head() to display the first few rows)
print(data_csv.head())

print(data_xls.columns)
data_xls["YEAR"] = pd.to_numeric(data_xls["YEAR"], errors="coerce")
data_xls["TOTAL HA (ADJUSTED_HA)"]=pd.to_numeric(data_xls["TOTAL HA (ADJUSTED_HA)"], errors="coerce")

data_xls = data_xls.dropna(subset=["YEAR", "TOTAL HA (ADJUSTED_HA)"])

sns.set_style("whitegrid")

plt.figure(figsize=(20,10))
plt.bar(data_xls['YEAR'], data_xls['TOTAL HA (ADJUSTED_HA)'], color="#00BAFF", alpha=0.4)
plt.plot(data_xls['YEAR'], data_xls["TOTAL HA (ADJUSTED_HA)"], color = "#003DBF", alpha=0.6, linewidth = 3)


plt.title=("Number of Fires and Area Burned in Canada by Year")
plt.suptitle=("Source: Canadian National Fire Database (CNFDB)")
plt.xlabel=("Years")
plt.ylabel=("Area Burned (millions of hectares)")
plt.yscale = (1*(10**6))
plt.yticks=1
plt.grid = (True)

plt.show()
