#read specific columns from a given csv file and print their components
import pandas as pd
columns = ["Maxpulse"]
file = pd.read_csv("sample.csv", usecols=columns)
print(file)
