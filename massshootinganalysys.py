import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb

sb.set()
data=pd.read_csv("Mass Shootings Dataset Ver 5.csv")
# print(data.describe)
# sb.scatterplot(data, x="Latitude", y="Longitude", hue="Gender")
# plt.show()
print(data[data["Injured"]==527])
