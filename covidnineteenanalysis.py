import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("country_wise_latest.csv")
print(data.head(5))
print(data.info())
print(data.describe())
print(data.isnull().sum())#check null values
data.fillna(value=0, inplace=True)