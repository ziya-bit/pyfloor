import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("charcters_stats.csv")
print(data)
good=data[data["Alignment"]=="good"]
evil=data[data["Alignment"]=="bad"]
neutral=data[data["Alignment"]=="neutral"]

print(good)
print(evil)
print(neutral)

print(data["Alignment"].value_counts())

print(evil.sort_values(by=["Combat"], ascending=False).head(10))