import pandas as pd
import numpy as np
import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

import seaborn as sns


print("Setup Complete")
path_data = "/kaggle/input/videogamesales/vgsales.csv"
file_data = pd.read_csv("/kaggle/input/videogamesales/vgsales.csv")
file_data.head()

plt.figure(figsize=(15, 10))
sns.countplot(x="Year", data = file_data, order = file_data.groupby(by=['Year'])['Name'].count().sort_values(ascending=False).index)
plt.xticks(rotation=90)