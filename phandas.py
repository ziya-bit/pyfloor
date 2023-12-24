import pandas as pd
data=pd.read_csv("birds.csv")
print(data)
print(data.info())
print(data["scientific name"].tail(15))
print(data["scientific name"].unique())
