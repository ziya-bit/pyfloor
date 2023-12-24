import matplotlib.pyplot as pp
import numpy as np
import pandas as pd
import seaborn as sb

# data=np.linspace(0, 10, 100)
# sb.set()
# pp.plot(data, np.sin(data), data, np.cos(data))
# pp.show()

sb.set()
data=sb.load_dataset("iris")
print(data.head())
sb.catplot(x="species",y="sepal_width",data=data, kind="violin")
pp.show()
