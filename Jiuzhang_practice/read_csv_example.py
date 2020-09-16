import pandas as pd
import numpy as np
df = pd.read_csv('example.csv', header=0)
df0 = df.sort_values(by='timestamp')
data = []
for i in range(len(df0)):
    data.append([df0.iloc[i].id, df0.iloc[i].timestamp, df0.iloc[i].birate])




