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

goodmax=good.sort_values(by=["Total"], ascending=False)
plt.figure(figsize=(8,5))
plt.bar(list(goodmax["Name"])[0:5],list(goodmax["Total"])[0:5])
# plt.show()

plt.figure(figsize=(5,7))
plt.hist(evil["Total"], bins=50)
plt.title("villains IQ")
plt.xlabel("IQ")
# plt.show()

darkseid=evil[evil["Name"]=="Darkseid"]
darkseidlist=list(darkseid.values)
darkseidlist=darkseidlist[0][2:8]
labels=list(darkseid.columns.values)
labels=labels[2:8]
plt.pie(darkseidlist, labels=labels)
plt.show()